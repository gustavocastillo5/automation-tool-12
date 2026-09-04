import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name="autoclicker", log_file="logs/autoclicker.log", max_bytes=1048576, backup_count=5):
    """
    Configures and returns a logger with both console and rotating file handlers.
    """
    # Ensure the log directory exists before initializing the file handler
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Prevent duplicate handlers if the logger is re-initialized
    if logger.hasHandlers():
        logger.handlers.clear()

    # Setup formatting for file and console logs
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_formatter = logging.Formatter(
        '%(levelname)s: %(message)s'
    )

    # Configure the rotating file handler for detailed debugging logs
    file_handler = RotatingFileHandler(
        log_file, maxBytes=max_bytes, backupCount=backup_count, encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)

    # Configure the stream handler for clean stdout display
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_formatter)

    # Register both handlers to the logger instance
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
