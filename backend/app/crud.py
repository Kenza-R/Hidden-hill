"""Database helpers for common Hidden Hill operations."""

from __future__ import annotations

from typing import Optional

from sqlalchemy.orm import Session, joinedload

from . import models


def get_or_create_user(db: Session, email: str) -> models.User:
    user = db.query(models.User).filter(models.User.email == email).one_or_none()
    if user:
        return user

    user = models.User(email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def create_video_with_job(db: Session, pubmed_id: str, user: Optional[models.User]) -> models.Job:
    video = models.Video(pubmed_id=pubmed_id, user=user)
    job = models.Job(video=video)
    db.add(video)
    db.add(job)
    db.commit()
    db.refresh(job)
    db.refresh(video)
    return job


def get_job_with_video(db: Session, job_id: str) -> Optional[models.Job]:
    return (
        db.query(models.Job)
        .options(joinedload(models.Job.video))
        .filter(models.Job.id == job_id)
        .one_or_none()
    )


def list_videos(db: Session, limit: int = 50) -> list[models.Video]:
    return (
        db.query(models.Video)
        .order_by(models.Video.created_at.desc())
        .limit(limit)
        .all()
    )
