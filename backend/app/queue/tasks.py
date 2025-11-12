"""Celery task definitions."""

from __future__ import annotations

from celery.utils.log import get_task_logger

from .. import crud
from ..database import SessionLocal
from .celery_app import celery_app
from .progress import JobProgressReporter

logger = get_task_logger(__name__)


@celery_app.task(bind=True, name="videos.generate")
def generate_video_task(self, job_id: str, pubmed_id: str) -> dict:
    """Skeleton video generation task (Task 2)."""
    session = SessionLocal()
    reporter = JobProgressReporter(job_id)

    try:
        crud.update_job(
            session,
            job_id,
            status="processing",
            progress=5,
            celery_task_id=self.request.id,
        )
        reporter.update(progress=25)

        # TODO: Integrate professor's video generation pipeline.
        reporter.update(progress=90)

        crud.update_job(session, job_id, status="completed", progress=100)
        logger.info("Completed job %s for pubmed_id=%s", job_id, pubmed_id)
        return {"job_id": job_id, "status": "completed"}
    except Exception as exc:  # pragma: no cover - defensive logging
        logger.exception("Job %s failed: %s", job_id, exc)
        crud.update_job(session, job_id, status="failed", error_message=str(exc))
        raise
    finally:
        session.close()
