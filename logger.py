import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = "logs"
LOG_FILE = "autoclicker.log"
MAX_BYTES = 2 * 1024 * 1024  # 2 MB size limit per log file
BACKUP_COUNT = 5  # Keep up to 5 historical log files


def setup_logger(name: str = "autoclicker", level: int = logging.INFO) -> logging.Logger:
    """Configures and returns a logger with console and rotating file handlers."""
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent adding duplicate handlers on multiple calls
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Stream handler for stdout console output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Rotating file handler for persistent logs
    log_path = os.path.join(LOG_DIR, LOG_FILE)
    file_handler = RotatingFileHandler(
        log_path,
        maxBytes=MAX_BYTES,
        backupCount=BACKUP_COUNT,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


# Initialize primary application logger
app_logger = setup_logger()
