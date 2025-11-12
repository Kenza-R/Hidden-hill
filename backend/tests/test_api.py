"""Tests for FastAPI endpoints with eager Celery tasks."""

from __future__ import annotations

import time

import pytest


def test_api_generate_and_poll_eager(test_client, db_session):
    """Test full API flow: generate job, poll until completed."""
    # Create a job via API
    response = test_client.post(
        "/api/videos/generate",
        json={"pubmed_id": "PMC10979640"},
    )
    assert response.status_code == 201
    data = response.json()
    job_id = data["job_id"]
    assert data["status"] == "queued"

    # Poll status until completed (should be immediate in eager mode)
    max_attempts = 10
    for attempt in range(max_attempts):
        response = test_client.get(f"/api/videos/{job_id}")
        assert response.status_code == 200
        data = response.json()

        if data["status"] == "completed":
            assert data["progress"] == 100
            assert data["video"]["video_url"] == "s3://fake/video.mp4"
            assert data["video"]["status"] == "completed"
            break

        # In eager mode, should complete immediately, but allow small delay
        if attempt < max_attempts - 1:
            time.sleep(0.1)
    else:
        pytest.fail(f"Job {job_id} did not complete within {max_attempts} attempts")

