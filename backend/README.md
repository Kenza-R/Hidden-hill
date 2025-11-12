# Hidden Hill Backend

FastAPI service that powers Sprint 2 Task 1. It exposes the video generation endpoints, manages database models, and coordinates with later Celery jobs.

## ✅ Status: TASK 1 COMPLETE

All core functionality is implemented and tested:
- FastAPI server running
- PostgreSQL database connected and working
- All API endpoints functional
- Input validation and error handling working
- Swagger documentation accessible
- Database CRUD operations verified

## Setup

1. Create and activate a Python 3.11+ virtualenv.
2. Install dependencies: `pip install -r requirements.txt`.
3. Copy `.env.example` to `.env` and update secrets.
4. Run the development server: `uvicorn main:app --reload`.

## Local Services

Start PostgreSQL (Homebrew service) and create the database before running the API:

```bash
brew services start postgresql@14
createdb hidden_hill_db
```

## Running the Server

```bash
source .venv/bin/activate
uvicorn main:app --reload --port 8000
```

Server runs on `http://localhost:8000`
Swagger API docs: `http://localhost:8000/docs`

## API Endpoints

### Health Check
- `GET /health/` - Returns `{"status": "ok"}`

### Video Generation
- `POST /api/videos/generate` - Create a new video generation job
  ```json
  {
    "pubmed_id": "PMC10979640",
    "user_email": "optional@example.com"
  }
  ```
  Returns: `{"job_id": "...", "video_id": "...", "status": "pending"}`

### Status Check
- `GET /api/videos/{job_id}` - Get current job status
  Returns: `{"job_id": "...", "status": "pending", "progress": 0, "video": {...}}`

### Download Video
- `GET /api/videos/{job_id}/download` - Download generated video (when complete)

## Database Schema

Three tables are automatically created:

1. **users** - Store user emails (optional)
2. **videos** - Store video metadata (pubmed_id, status, video_url)
3. **jobs** - Track job progress and celery task IDs

## Next Steps

- Implement Celery + Redis queue (Task 2)
- Connect frontend to API (Task 4)
- Set up Docker deployment (Task 5)
