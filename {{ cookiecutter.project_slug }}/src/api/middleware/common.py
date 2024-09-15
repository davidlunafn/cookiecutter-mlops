from fastapi import Request
from main import app
import time

@app.middleware("http")
async def log_response_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(f"Request to {request.url.path} took {process_time:.4f} seconds")
    response.headers["X-Process-Time"] = str(process_time)

    return response
