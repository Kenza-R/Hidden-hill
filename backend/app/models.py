"""SQLAlchemy models for Hidden Hill entities."""

from __future__ import annotations

from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


def default_uuid() -> str:
    return str(uuid4())


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    videos = relationship("Video", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<User id={self.id} email={self.email}>"


class Video(Base):
    __tablename__ = "videos"

    id = Column(String, primary_key=True, default=default_uuid)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    pubmed_id = Column(String, nullable=False)
    status = Column(String, nullable=False, default="pending")
    video_url = Column(String, nullable=True)
    error_message = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="videos")
    job = relationship("Job", back_populates="video", uselist=False, cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Video id={self.id} pubmed_id={self.pubmed_id} status={self.status}>"


class Job(Base):
    __tablename__ = "jobs"

    id = Column(String, primary_key=True, default=default_uuid)
    video_id = Column(String, ForeignKey("videos.id"), nullable=False)
    status = Column(String, nullable=False, default="pending")
    progress = Column(Integer, nullable=False, default=0)
    celery_task_id = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    video = relationship("Video", back_populates="job")

    def __repr__(self) -> str:
        return f"<Job id={self.id} status={self.status} progress={self.progress}>"
