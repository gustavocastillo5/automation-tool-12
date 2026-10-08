import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name: str = "autoclicker", log_file: str = "autoclicker.log") -> logging.Logger:
    """
    Configures and returns a logger with console and rotating file handlers.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Prevent adding handlers multiple times
    if logger.handlers:
        return logger

    # Unified formatting for output
    log_format = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console handler for standard output (INFO level)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    # Rotating file handler for debugging (DEBUG level, max 5MB, 3 backups)
    try:
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=5 * 1024 * 1024,  # 5 MB limit
            backupCount=3,
            encoding="utf-8"
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)
    except OSError as e:
        logger.warning(f"Failed to initialize rotating file log: {e}")

    return logger

# Default instantiated logger for immediate use across module
log = setup_logger()
