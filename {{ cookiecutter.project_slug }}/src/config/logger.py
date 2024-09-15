from pydantic import BaseModel
from .config import config
import logging
from logging.config import dictConfig

class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "uvicorn"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"

    # Logging config
    version: int = 1
    disable_existing_loggers: bool = False
    formatters: dict = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers: dict = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers: dict = {
        LOGGER_NAME: {
          "handlers": ["default"],
          "level": LOG_LEVEL,
          "propagate": False},
        config.PROJECT_NAME: {
            "handlers": ["default"],
            "level": LOG_LEVEL,
            "propagate": False
        }
    }

dictConfig(LogConfig().model_dump())
logger = logging.getLogger(config.PROJECT_NAME)
logger.info("Configuration finished")
