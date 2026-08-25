import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name="autoclicker", log_dir="logs", log_file="autoclicker.log", level=logging.INFO, max_bytes=10485760, backup_count=5):
    """Configure logger with file rotation for the autoclicker tool."""
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_path = os.path.join(log_dir, log_file)
    logger = logging.getLogger(name)
    # Clear existing handlers to prevent duplicates
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.setLevel(level)
    # Set up rotating file handler
    file_handler = RotatingFileHandler(
        log_path, maxBytes=max_bytes, backupCount=backup_count
    )
    file_handler.setLevel(level)
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    # Add stream handler for console output
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger

# For direct testing
if __name__ == "__main__":
    log = setup_logger()
    log.debug("Debug message example")
    log.info("Info message example")
    log.warning("Warning message example")
    log.error("Error message example")