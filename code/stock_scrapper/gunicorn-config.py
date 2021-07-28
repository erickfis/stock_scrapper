"""Configuration for gunicorn."""

import os

timeout = 2000
bind = f":{os.environ.get('PORT', '8000')}"
worker_class = "uvicorn.workers.UvicornWorker"
