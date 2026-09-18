import os
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_filename="autoclicker.log", max_bytes=5242880, backup_count=3):
    """
    Sets up a rotating file logger and a console logger for the autoclicker.
    """
    logger = logging.getLogger("autoclicker")
    logger.setLevel(logging.DEBUG)

    # Clear existing handlers to avoid duplicate log entries
    if logger.hasHandlers():
        logger.handlers.clear()

    # Formatters for consistent log structure
    log_format = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console handler for real-time CLI feedback during operations
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    # Extract directory path and create if necessary
    log_dir = os.path.dirname(log_filename)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Rotating file handler to manage disk space for persistent session logs
    try:
        file_handler = RotatingFileHandler(
            log_filename,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8"
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)
    except (OSError, PermissionError) as e:
        console_handler.warning(f"Could not initialize file logging: {e}. Falling back to console.")

    return logger
