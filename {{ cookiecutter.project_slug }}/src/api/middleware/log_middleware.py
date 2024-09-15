from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response, FastAPI
import time
from src.config.logger import logger  # Asegúrate de tener configurado el logger

class ResponseTimeMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response:
        # Registrar el tiempo de inicio
        start_time = time.time()

        # Ejecutar el siguiente middleware o endpoint
        response = await call_next(request)

        # Calcular el tiempo transcurrido
        process_time = time.time() - start_time

        # Log el tiempo de respuesta
        logger.info(f"Request to {request.url.path} took {process_time:.4f} seconds")

        # Agregar el tiempo de respuesta a los headers
        response.headers["X-Process-Time"] = str(process_time)

        return response
