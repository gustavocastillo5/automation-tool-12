import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file="autoclicker.log", max_bytes=1048576, backup_count=5):
    """
    Configures and returns a rotating logger for the autoclicker application.
    """
    logger = logging.getLogger("autoclicker")
    logger.setLevel(logging.DEBUG)

    # Avoid adding duplicate handlers if logger is already configured
    if logger.handlers:
        return logger

    # Create log directory if it does not exist
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s [%(name)s:%(filename)s:%(lineno)d] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # File Handler with rotation
    file_handler = RotatingFileHandler(
        log_file, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console Handler for real-time terminal feedback
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

# Default logger instance ready for import across modules
log = setup_logger()
