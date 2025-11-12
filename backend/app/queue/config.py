"""Configuration helpers for Celery queue."""

from __future__ import annotations

import os
from functools import lru_cache


class Settings:
    """Load queue-related configuration from environment variables."""

    def __init__(self) -> None:
        redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
        self.celery_broker_url = os.getenv("CELERY_BROKER_URL", redis_url)
        self.celery_result_backend = os.getenv("CELERY_RESULT_BACKEND", redis_url)
        self.celery_default_queue = os.getenv("CELERY_DEFAULT_QUEUE", "hidden-hill")


@lru_cache()
def get_settings() -> Settings:
    """Return cached settings instance."""
    return Settings()
