import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(
    name: str = "autoclicker",
    log_file: str = "autoclicker.log",
    level: int = logging.INFO,
    max_bytes: int = 5 * 1024 * 1024,
    backup_count: int = 3
) -> logging.Logger:
    """Sets up a rotating file logger and a console logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if already configured
    if logger.handlers:
        return logger

    # Ensure directory structure for logs exists
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Setup console output handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Setup rotating file handler for disk storage
    try:
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8"
        )
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except IOError as e:
        logger.warning(f"Failed to initialize file logging: {e}. Console logging only.")

    return logger
