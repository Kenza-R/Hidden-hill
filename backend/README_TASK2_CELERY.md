# Task 2 – Celery Queue README

## 1. Why Celery?

- **Problem**: Generating a video can take several minutes. Running it inside the FastAPI request would block the worker, time out clients, and prevent horizontal scaling.
- **Solution**: Celery offloads long-running work to background workers. The API immediately responds with a job ID; workers pick up the task asynchronously and update status as they go.
- **Benefits**: Non-blocking API, retriable jobs, progress tracking, and easier scaling—run more Celery workers when load increases.

## 2. Architecture (FastAPI ⇆ Redis ⇆ Celery)

```
Client → FastAPI → Redis (broker) → Celery Worker → PostgreSQL + Storage
                 ↘ Redis (result backend / status cache)
```

- `POST /api/videos/generate` enqueues a Celery task (`generate_video_task`) with parameters (job_id, video_id, pubmed_id).
- Redis acts as both **broker** (queue) and **result backend** (optional but convenient for traces).
- The Celery worker imports the professor’s pipeline wrapper, processes the job, updates the database via SQLAlchemy, and stores the rendered video URL.
- FastAPI polling endpoint (`GET /api/videos/{job_id}`) reads the latest job state from PostgreSQL; optionally, a lightweight cache in Redis can store intermediate progress emitted by Celery.

## 3. File Structure

Create the following under `backend/app/`:

```
backend/
  app/
    core/
      __init__.py
      config.py          # shared settings (Redis URL, Celery broker URL)
    workers/
      __init__.py
      celery_app.py      # Celery instance factory + autodiscovery
      tasks.py           # generate_video_task definition
    services/
      __init__.py
      video_pipeline.py  # wrapper around professor's CLI
    utils/
      __init__.py
      progress.py        # helper to push progress updates
```

Updates needed in existing files:

- `app/database.py`: expose `SessionLocal` for workers.
- `app/crud.py`: add functions `update_job_status`, `set_video_url`, etc.
- `app/routers/videos.py`: enqueue Celery task and return job ID.
- `backend/__main__.py` (optional): entrypoint to run both API and worker via CLI.

## 4. Setup & Run

Ensure Redis is running locally (default port `6379`).

```bash
# 1. Install deps (inside backend virtualenv)
pip install celery[redis] redis

# 2. Export environment variables
export REDIS_URL="redis://localhost:6379/0"
export CELERY_BROKER_URL="$REDIS_URL"
export CELERY_RESULT_BACKEND="$REDIS_URL"

# 3. Start FastAPI (terminal 1)
cd backend
uvicorn main:app --reload --port 8000

# 4. Start Celery worker (terminal 2)
celery -A app.workers.celery_app.celery_app worker --loglevel=info
```

Optional: start a Celery beat scheduler for periodic cleanup.

```bash
celery -A app.workers.celery_app.celery_app beat --loglevel=info
```

## 5. How to Test

1. **Unit tests**: create tests under `backend/tests/` that:
   - Mock the pipeline and assert `generate_video_task` updates job status.
   - Use Celery’s `app.task(bind=True)` + `shared_task` to test progress updates.
2. **Integration test**:
   - Start Redis + worker.
   - Call `POST /api/videos/generate`.
   - Poll `GET /api/videos/{job_id}` until status becomes `completed`.
   - Verify `video.video_url` is not `null`.
3. **Manual**:
   - Watch worker logs for progress messages.
   - Inspect Redis queue (`redis-cli monitor`) to confirm tasks enqueued.

For CI, use Celery’s `CELERY_TASK_ALWAYS_EAGER=true` to execute tasks synchronously during tests.

## 6. Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| `celery.exceptions.OperationalError: Error 111 connecting to localhost:6379` | Redis not running or wrong URL | Start Redis `brew services start redis` or update `REDIS_URL`. |
| Task never finishes | Worker not running or failed import of pipeline | Check worker terminal; confirm PYTHONPATH includes `backend`. |
| `Can't pickle function` errors | Task defined inside a function / lambda | Define tasks at module top-level. |
| Job stuck in `PENDING` | Result backend not configured | Set `CELERY_RESULT_BACKEND` to Redis or rely on DB status updates. |
| Database session errors in worker | Session not scoped correctly | Use `SessionLocal()` inside task; ensure `session.close()` in finally block. |
| Progress not updating | No Redis writes | Ensure task calls `progress.publish(job_id, step)`; check Redis keys. |

If stuck, run worker with `--loglevel=debug` and enable Celery Flower (`celery -A ... flower`) for web-based monitoring.

