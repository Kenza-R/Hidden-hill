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

### Redis (via Docker Compose)

Start Redis using Docker Compose:

```bash
# From repo root
docker compose up -d redis
```

Redis will be available at `redis://localhost:6379/0`.

### PostgreSQL

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
- `GET /api/health` - Returns `{"api": "ok", "redis": <bool>, "celery_ping": <bool>}`

### Video Generation
- `POST /api/videos/generate` - Create a new video generation job
  ```json
  {
    "pubmed_id": "PMC10979640",
    "user_email": "optional@example.com"
  }
  ```
Returns: `{"job_id": "...", "video_id": "...", "status": "queued"}`

### Status Check
- `GET /api/videos/{job_id}` - Get current job status
Returns: `{"job_id": "...", "status": "processing", "progress": 50, "video": {...}}`

### Download Video
- `GET /api/videos/{job_id}/download` - Download generated video (when complete)

## Database Schema

Three tables are automatically created:

1. **users** - Store user emails (optional)
2. **videos** - Store video metadata (pubmed_id, status, video_url)
3. **jobs** - Track job progress and celery task IDs

## Celery Queue

**Why**: Video generation can take minutes. Celery lets FastAPI return immediately while workers run the heavy pipeline and update status progressively.

**How it works**:
- FastAPI enqueues `videos.generate` with `generate_video_task.delay(job_id, pubmed_id)`.
- Redis (env: `CELERY_BROKER_URL` / `CELERY_RESULT_BACKEND`) carries messages between API and workers.
- Workers update PostgreSQL progress via `JobProgressReporter`, keeping `/api/videos/{job_id}` in sync.

**Setup**:
1. Install queue deps: `pip install -r requirements.txt` (includes `celery`, `redis`).
2. Export env vars (examples):
   ```bash
   export REDIS_URL=redis://localhost:6379/0
   export CELERY_BROKER_URL=$REDIS_URL
   export CELERY_RESULT_BACKEND=$REDIS_URL
   ```

**Run**:
```bash
# Terminal 1: Start API
uvicorn main:app --reload --port 8000

# Terminal 2: Start Celery worker
celery -A app.queue.celery_app worker --loglevel=info
```

**Optional: Flower (Celery Monitoring)**

Monitor Celery tasks and workers via Flower web UI:

```bash
# Start Flower (from repo root)
docker compose --profile monitoring up -d flower
```

Access Flower at `http://localhost:5555` to view:
- Active tasks and workers
- Task history and statistics
- Worker status and resource usage

**Test**:
- Local manual: call `POST /api/videos/generate`, poll `/api/videos/{job_id}` and watch worker logs.
- Automated: run `pytest` from `backend/` directory (uses eager mode, no Redis/worker needed).

**Quick Smoke Test**:
```bash
# 1. Start API (terminal 1)
uvicorn main:app --reload --port 8000

# 2. Start worker (terminal 2)
celery -A app.queue.celery_app worker --loglevel=info

# 3. Create a job
curl -X POST http://localhost:8000/api/videos/generate \
  -H "Content-Type: application/json" \
  -d '{"pubmed_id": "PMC10979640"}'

# 4. Poll status (replace JOB_ID from step 3)
curl http://localhost:8000/api/videos/JOB_ID

# 5. Check health
curl http://localhost:8000/api/health
```

**Troubleshooting**:
- **Redis off / Connection refused** → Start Redis: `docker compose up -d redis` (or ensure Redis is running and `REDIS_URL` matches).
- **Worker not running** → Job stuck `queued`; start worker: `celery -A app.queue.celery_app worker --loglevel=info`. Check worker logs for import errors.
- **Pickling errors** (`Can't pickle function`) → Tasks must be defined at module top-level, not inside functions/lambdas. Ensure `generate_video_task` is at `app.queue.tasks` module level.
- **Task crashes** → Check worker log; failures set job/video status to `failed` with error message.

## Running Tests

### Unit Tests (Default)
```bash
cd backend
pytest
```

Tests run with `CELERY_TASK_ALWAYS_EAGER=true` (no Redis/worker needed). Uses in-memory SQLite.

### Integration Tests (Optional)
Integration tests require real Redis and a running worker:

```bash
cd backend
REDIS_URL=redis://localhost:6379/0 TEST_INTEGRATION=1 pytest -k integration
```

**Prerequisites:**
- Redis running on `localhost:6379` (or set `REDIS_URL`)
- Worker will be started automatically by the test fixture
- Uses real database (PostgreSQL via `TEST_DATABASE_URL` or SQLite file)

**Note:** Integration tests are skipped by default. Set `TEST_INTEGRATION=1` to enable.

## Next Steps

- Plug professor's pipeline into `generate_video_task`
- Connect frontend to API (Task 4)
- Set up Docker deployment (Task 5)
