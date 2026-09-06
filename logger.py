import os
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name="autoclicker", log_file="autoclicker.log", level=logging.INFO):
    """
    Configures and returns a logger with both console and rotating file handlers.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if logger is already configured
    if logger.hasHandlers():
        return logger

    # Create formatters
    log_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    # Rotating File Handler (max 5MB per file, keeping up to 3 backups)
    try:
        # Ensure log directory exists if a path is provided
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=5 * 1024 * 1024,  # 5 MB
            backupCount=3,
            encoding="utf-8"
        )
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)
    except Exception as e:
        logger.warning(f"Failed to set up file logging: {e}")

    return logger

if __name__ == "__main__":
    app_logger = setup_logger()
    app_logger.info("Autoclicker logger initialized successfully.")
