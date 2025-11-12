"""Pydantic schemas for API requests and responses."""

from __future__ import annotations

from datetime import datetime

from typing import Optional

from pydantic import BaseModel, EmailStr, Field, field_validator


class HealthResponse(BaseModel):
    status: str = "ok"


class VideoGenerateRequest(BaseModel):
    pubmed_id: str = Field(..., min_length=3, description="PubMed, PMC, or PMID identifier")
    user_email: Optional[EmailStr] = Field(
        default=None, description="Optional email to tie the video to a user"
    )

    @field_validator("pubmed_id")
    @classmethod
    def _normalize_pubmed_id(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("PubMed ID cannot be empty")
        return cleaned


class JobCreateResponse(BaseModel):
    job_id: str
    video_id: str
    status: str


class VideoMetadata(BaseModel):
    id: str = Field(alias="id")
    pubmed_id: str
    status: str
    video_url: Optional[str] = None
    error_message: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
        populate_by_name = True


class JobStatusResponse(BaseModel):
    job_id: str
    status: str
    progress: int
    video: VideoMetadata

    class Config:
        from_attributes = True
