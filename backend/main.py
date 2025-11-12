from fastapi import FastAPI

from app.database import Base, engine
from app.routers import health, videos

# Ensure tables exist during early development; migrations will replace this later.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Hidden Hill API",
    version="0.1.0",
    description="Backend service for converting PubMed papers into shareable videos.",
)

app.include_router(health.router)
app.include_router(videos.router)


@app.get("/", tags=["root"])
def read_root() -> dict[str, str]:
    """Simple sanity endpoint for local development."""
    return {"message": "Hidden Hill API is running"}
