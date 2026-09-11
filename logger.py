import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = "logs"
LOG_FILE = "autoclicker.log"
MAX_BYTES = 1_048_576  # 1 MB log file limit
BACKUP_COUNT = 5       # Keep up to 5 historical log files

def setup_logger(name: str = "autoclicker", log_level: int = logging.INFO) -> logging.Logger:
    """Configures and returns a logger with console and rotating file handlers."""
    os.makedirs(LOG_DIR, exist_ok=True)
    log_path = os.path.join(LOG_DIR, LOG_FILE)

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Prevent adding duplicate handlers if function is invoked multiple times
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console output handler for live CLI monitoring
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(log_level)
    logger.addHandler(console_handler)

    # Rotating file handler to prevent excessive disk usage
    file_handler = RotatingFileHandler(
        log_path,
        maxBytes=MAX_BYTES,
        backupCount=BACKUP_COUNT,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(log_level)
    logger.addHandler(file_handler)

    return logger

# Default logger instance for the automation tool
logger = setup_logger()
