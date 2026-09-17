import logging
from logging.handlers import RotatingFileHandler
import os

LOG_FILE = "automation.log"
MAX_BYTES = 5 * 1024 * 1024  # 5MB
BACKUP_COUNT = 3

def setup_logger(name: str = "automation-tool-12") -> logging.Logger:
    """Initializes a rotating file logger for the application."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # File handler with rotation
        file_handler = RotatingFileHandler(
            LOG_FILE, 
            maxBytes=MAX_BYTES, 
            backupCount=BACKUP_COUNT
        )
        file_handler.setFormatter(formatter)

        # Console handler for real-time visibility
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger