"""Helpers for reporting job progress from Celery tasks."""

from __future__ import annotations

from typing import Optional

from .. import crud
from ..database import SessionLocal


class JobProgressReporter:
    """Persist incremental job progress updates."""

    def __init__(self, job_id: str) -> None:
        self.job_id = job_id

    def update(self, progress: int, status: Optional[str] = None) -> None:
        session = SessionLocal()
        try:
            crud.update_job(session, self.job_id, progress=progress, status=status)
        finally:
            session.close()
