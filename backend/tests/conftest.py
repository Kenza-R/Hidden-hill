"""Pytest fixtures for backend tests."""

from __future__ import annotations

from typing import Generator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.models import Job, User, Video


@pytest.fixture(scope="function")
def db_session() -> Generator:
    """Create an in-memory SQLite database session for testing."""
    # Use in-memory SQLite for tests
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)
    TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def test_client(db_session):
    """Create a FastAPI test client with database dependency override."""
    from fastapi.testclient import TestClient
    from main import app

    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


@pytest.fixture
def sample_job(db_session) -> Job:
    """Create a sample job with video for testing."""
    user = User(email="test@example.com")
    video = Video(pubmed_id="PMC10979640", user=user)
    job = Job(video=video, status="pending", progress=0)
    db_session.add(user)
    db_session.add(video)
    db_session.add(job)
    db_session.commit()
    db_session.refresh(job)
    return job

