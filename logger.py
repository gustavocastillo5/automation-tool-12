import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logger(
    name: str = "autoclicker",
    log_dir: str = "logs",
    log_file: str = "autoclicker.log",
    max_bytes: int = 1024 * 1024,
    backup_count: int = 3,
    level: int = logging.INFO,
) -> logging.Logger:
    """Configures and returns a logger instance with stream and rotating file output."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if re-initialized
    if logger.handlers:
        return logger

    # Ensure target directory exists
    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)
    full_path = log_path / log_file

    # Standard output formatting
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console output handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    logger.addHandler(console_handler)

    # Size-based rotating log file handler
    file_handler = RotatingFileHandler(
        filename=full_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)
    logger.addHandler(file_handler)

    return logger


# Default logger instance for direct import across modules
logger = setup_logger()
