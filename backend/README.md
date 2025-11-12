# Hidden Hill Backend

FastAPI service that powers Sprint 2 Task 1. It exposes the video generation endpoints, manages database models, and coordinates with later Celery jobs.

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

## Next Steps

- Configure PostgreSQL and run Alembic migrations (coming later in the sprint).
- Hook up Celery and Redis for Task 2.
