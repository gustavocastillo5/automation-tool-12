import logging
import logging.handlers
import os

# Configure application logging with rotation
# Keeps 5 files of 1MB each to manage disk space

LOG_FILE = "automation.log"
MAX_BYTES = 1024 * 1024
BACKUP_COUNT = 5

def setup_logger(name: str = "automation-tool") -> logging.Logger:
    """Initializes a rotating file logger for the application."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers on re-initialization
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Rotating file handler configuration
        file_handler = logging.handlers.RotatingFileHandler(
            LOG_FILE,
            maxBytes=MAX_BYTES,
            backupCount=BACKUP_COUNT
        )
        file_handler.setFormatter(formatter)
        
        # Console handler for real-time output
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger