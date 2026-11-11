import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from typing import Optional


def setup_logger(
    name: str = "autoclicker",
    log_file: Optional[str] = "autoclicker.log",
    level: int = logging.INFO
) -> logging.Logger:
    """Configures application logger with fallback stream output if file system errors occur."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s - %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Always attach console output as primary or standard fallback
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if log_file:
        try:
            log_dir = os.path.dirname(log_file)
            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir, exist_ok=True)

            file_handler = RotatingFileHandler(
                log_file, maxBytes=1_000_000, backupCount=3, encoding="utf-8"
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except (PermissionError, OSError, ValueError) as err:
            logger.warning(
                f"Failed to set up log file '{log_file}': {err}. "
                "Falling back to stdout logging only."
            )

    return logger


def safe_log_event(logger: logging.Logger, level: int, message: str) -> None:
    """Safely logs messages handling unhandled formatting or stream exceptions."""
    try:
        if not isinstance(message, str):
            message = str(message)
        logger.log(level, message)
    except Exception as err:
        # Edge case: prevent logging mechanism itself from breaking the main click loop
        sys.stderr.write(f"Logging system failure: {err}\n")
