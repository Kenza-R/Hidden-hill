"""Health check endpoint."""

from fastapi import APIRouter

from .. import schemas

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/", response_model=schemas.HealthResponse)
def health_check() -> schemas.HealthResponse:
    """Return a simple OK payload for uptime checks."""
    return schemas.HealthResponse()
