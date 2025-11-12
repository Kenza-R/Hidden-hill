"""CLI helper to run API or worker from `python -m backend`."""

from __future__ import annotations

import sys
import subprocess


def run_api() -> None:
    """Start the FastAPI server."""
    subprocess.run(["uvicorn", "main:app", "--reload", "--port", "8000"])


def run_worker() -> None:
    """Start the Celery worker."""
    subprocess.run(["celery", "-A", "app.queue.celery_app", "worker", "--loglevel=info"])


def main() -> None:
    """Dispatch to API or worker based on command."""
    if len(sys.argv) < 2:
        print("Usage: python -m backend [api|worker]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "api":
        run_api()
    elif command == "worker":
        run_worker()
    else:
        print(f"Unknown command: {command}")
        print("Usage: python -m backend [api|worker]")
        sys.exit(1)


if __name__ == "__main__":
    main()

