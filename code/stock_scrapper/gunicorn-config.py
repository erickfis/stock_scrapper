"""Configuration for gunicorn."""

import os

timeout = 20
bind = f":{os.environ.get('PORT', '8000')}"
worker_class = "uvicorn.workers.UvicornWorker"
