"""Integration tests that require real Redis and worker (skipped by default)."""

from __future__ import annotations

import os
import subprocess
import time

import pytest
import redis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from main import app


def _check_redis_available() -> bool:
    """Check if Redis is available."""
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    try:
        client = redis.from_url(redis_url, socket_connect_timeout=2)
        client.ping()
        return True
    except Exception:
        return False


@pytest.fixture(scope="module")
def integration_db():
    """Create a test database for integration tests."""
    # Use a real database connection (PostgreSQL or SQLite file)
    db_url = os.getenv("TEST_DATABASE_URL", "sqlite:///./test_integration.db")
    engine = create_engine(db_url, connect_args={"check_same_thread": False} if "sqlite" in db_url else {})
    Base.metadata.create_all(engine)
    TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

    yield TestingSessionLocal

    # Cleanup
    Base.metadata.drop_all(engine)
    if "sqlite" in db_url and os.path.exists("./test_integration.db"):
        os.remove("./test_integration.db")


@pytest.fixture(scope="module")
def worker_process():
    """Start a Celery worker process for integration tests."""
    # Start worker in background
    process = subprocess.Popen(
        ["celery", "-A", "app.queue.celery_app", "worker", "--loglevel=info", "--concurrency=1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    # Give worker time to start
    time.sleep(2)

    # Verify worker is running
    if process.poll() is not None:
        pytest.skip("Worker process failed to start")

    yield process

    # Cleanup: terminate worker
    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()


@pytest.fixture(scope="function")
def integration_client(integration_db, worker_process):
    """Create a test client with real database and worker."""
    from fastapi.testclient import TestClient

    def override_get_db():
        session = integration_db()
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


@pytest.mark.skipif(
    os.getenv("TEST_INTEGRATION") != "1" or not _check_redis_available(),
    reason="Integration tests require TEST_INTEGRATION=1 and Redis available",
)
def test_integration_generate_and_poll_real_worker(integration_client):
    """Integration test: enqueue via POST, poll GET until completed with real worker."""
    # Create a job via API (will enqueue to real Redis)
    response = integration_client.post(
        "/api/videos/generate",
        json={"pubmed_id": "PMC10979640"},
    )
    assert response.status_code == 201
    data = response.json()
    job_id = data["job_id"]
    assert data["status"] == "queued"

    # Poll status until completed (with exponential backoff)
    max_attempts = 30
    base_delay = 0.5
    max_delay = 5.0

    for attempt in range(max_attempts):
        response = integration_client.get(f"/api/videos/{job_id}")
        assert response.status_code == 200
        data = response.json()

        if data["status"] == "completed":
            assert data["progress"] == 100
            assert data["video"]["video_url"] == "s3://fake/video.mp4"
            assert data["video"]["status"] == "completed"
            return  # Success!

        if data["status"] == "failed":
            pytest.fail(f"Job {job_id} failed: {data.get('video', {}).get('error_message', 'Unknown error')}")

        # Exponential backoff: delay increases up to max_delay
        if attempt < max_attempts - 1:
            delay = min(base_delay * (2 ** attempt), max_delay)
            time.sleep(delay)

    pytest.fail(f"Job {job_id} did not complete within {max_attempts} attempts (status: {data.get('status')})")

