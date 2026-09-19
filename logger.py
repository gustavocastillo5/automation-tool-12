import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = "autoclicker", log_file: str = "automation.log") -> logging.Logger:
    """
    Configures a rotating file logger for the automation tool.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if setup is called multiple times
    if logger.hasHandlers():
        logger.handlers.clear()

    # Format logs with timestamps and levels
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # File rotation: 5MB per file, keep 3 backup files
    file_handler = RotatingFileHandler(
        log_file, 
        maxBytes=5 * 1024 * 1024, 
        backupCount=3
    )
    file_handler.setFormatter(formatter)

    # Console output for visibility during development
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Instantiate shared logger
automation_logger = setup_logger()