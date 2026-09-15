import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='automation-tool-12', log_file='app.log', level=logging.INFO):
    """Configures a rotating file logger for the application."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Ensure logs directory exists
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Setup rotation: 5MB per file, keep 3 backups
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=5 * 1024 * 1024, 
        backupCount=3
    )

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        logger.addHandler(handler)
        logger.addHandler(logging.StreamHandler())

    return logger

# Initialize global logger instance
app_logger = setup_logger()