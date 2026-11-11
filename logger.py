import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='automation-tool-12', log_file='app.log', level=logging.INFO):
    """
    Configures a rotating file logger for the automation tool.
    Limits log size to 5MB and keeps 3 backup files.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if setup is called multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotation setup: 5MB max, 3 backups
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Stream handler for console output
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

# Initialize default logger instance
log = setup_logger()