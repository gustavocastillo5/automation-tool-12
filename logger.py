import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='automation-tool', log_file='automation.log'):
    """Initializes a rotating file logger for the autoclicker."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotate logs after 1MB, keep 3 backup files
        file_handler = RotatingFileHandler(
            log_file, maxBytes=1*1024*1024, backupCount=3
        )
        file_handler.setFormatter(formatter)

        # Add stream handler for console output
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

# Instantiate default logger for the project
logger = setup_logger()