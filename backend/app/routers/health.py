"""Health check endpoint."""

from __future__ import annotations

import redis
from fastapi import APIRouter

from .. import schemas
from ..queue.celery_app import celery_app
from ..queue.config import get_settings

router = APIRouter(prefix="/api/health", tags=["health"])


def _check_redis() -> bool:
    """Ping Redis with a short timeout."""
    try:
        settings = get_settings()
        client = redis.from_url(settings.celery_broker_url, socket_connect_timeout=1)
        client.ping()
        client.close()
        return True
    except Exception:
        return False


def _check_celery() -> bool:
    """Ping Celery workers with a small timeout."""
    try:
        inspect = celery_app.control.inspect(timeout=1.0)
        result = inspect.ping()
        return result is not None and len(result) > 0
    except Exception:
        return False


@router.get("/", response_model=schemas.HealthDetailedResponse)
def health_check() -> schemas.HealthDetailedResponse:
    """Return detailed health status including Redis and Celery connectivity."""
    return schemas.HealthDetailedResponse(
        api="ok",
        redis=_check_redis(),
        celery_ping=_check_celery(),
    )
