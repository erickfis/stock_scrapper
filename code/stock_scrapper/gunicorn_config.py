import os

timeout = 60
bind = f":{os.environ.get('PORT', '8000')}"
worker_class = "uvicorn.workers.UvicornWorker"
