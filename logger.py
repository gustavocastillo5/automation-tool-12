import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='automation-tool-12', log_file='app.log'):
    """
    Configures a rotating file logger for the application.
    Limits file size to 5MB with 3 backup files.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if function is called multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # File rotation handler: max 5MB per file, keep 3 backups
        file_handler = RotatingFileHandler(
            log_file, maxBytes=5*1024*1024, backupCount=3
        )
        file_handler.setFormatter(formatter)

        # Console output for real-time monitoring
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

# Instantiate default logger for the tool
logger = setup_logger()