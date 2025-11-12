"""Tests for Celery task execution."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from app.queue.tasks import generate_video_task


def test_generate_video_task_sets_status_and_url(db_session, sample_job):
    """Test that the Celery task updates job status and sets video URL."""
    job_id = sample_job.id
    pubmed_id = sample_job.video.pubmed_id

    # Spy on the progress reporter
    with patch("app.queue.tasks.JobProgressReporter") as mock_reporter_class:
        mock_reporter = MagicMock()
        mock_reporter_class.return_value = mock_reporter

        # Execute the task directly (eager mode) - use apply() for synchronous execution
        result = generate_video_task.apply(args=(job_id, pubmed_id)).get()

        # Verify task returned success
        assert result["job_id"] == job_id
        assert result["status"] == "completed"

        # Verify progress reporter was called
        assert mock_reporter.update.call_count >= 2  # At least progress=25 and progress=90

    # Verify final state in database
    db_session.refresh(sample_job)
    assert sample_job.status == "completed"
    assert sample_job.progress == 100
    assert sample_job.video.status == "completed"
    assert sample_job.video.video_url == "s3://fake/video.mp4"

