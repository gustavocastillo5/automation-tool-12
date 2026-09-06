import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(
    log_file="autoclicker.log",
    level=logging.INFO,
    max_bytes=5 * 1024 * 1024,
    backup_count=3
):
    """Configures and returns a logger instance with file rotation."""
    logger = logging.getLogger("automation_tool")
    logger.setLevel(level)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

if __name__ == "__main__":
    app_logger = setup_logger()
    app_logger.info("Logger initialized successfully.")
