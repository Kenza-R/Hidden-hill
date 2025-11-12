"""Video-related API endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/api/videos", tags=["videos"])


@router.post("/generate", response_model=schemas.JobCreateResponse, status_code=status.HTTP_201_CREATED)
def generate_video(payload: schemas.VideoGenerateRequest, db: Session = Depends(get_db)) -> schemas.JobCreateResponse:
    """Create a Video + Job record and enqueue work (queue integration arrives in Task 2)."""
    user = None
    if payload.user_email:
        user = crud.get_or_create_user(db, payload.user_email)

    job = crud.create_video_with_job(db, pubmed_id=payload.pubmed_id, user=user)
    return schemas.JobCreateResponse(job_id=job.id, video_id=job.video_id, status=job.status)


@router.get("/{job_id}", response_model=schemas.JobStatusResponse)
def get_job_status(job_id: str, db: Session = Depends(get_db)) -> schemas.JobStatusResponse:
    job = crud.get_job_with_video(db, job_id)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")

    video = job.video
    return schemas.JobStatusResponse(
        job_id=job.id,
        status=job.status,
        progress=job.progress,
        video=schemas.VideoMetadata.model_validate(video),
    )


@router.get("/{job_id}/download")
def download_video(job_id: str, db: Session = Depends(get_db)) -> RedirectResponse:
    job = crud.get_job_with_video(db, job_id)
    if not job or not job.video:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")

    video = job.video
    if video.status != "completed" or not video.video_url:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Video not ready for download")

    return RedirectResponse(url=video.video_url)
