"""Celery app factory."""

from __future__ import annotations

from celery import Celery

from .config import get_settings

settings = get_settings()

celery_app = Celery(
    "hidden_hill",
    broker=settings.celery_broker_url,
    backend=settings.celery_result_backend,
)
celery_app.conf.task_default_queue = settings.celery_default_queue
celery_app.autodiscover_tasks(["app.queue"])
