import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name='automation-tool-12', log_file='app.log', level=logging.INFO):
    """Configures a rotating file logger for the application."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Ensure logs directory exists
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Setup rotation: 5MB per file, keep 3 backup files
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=5*1024*1024, 
        backupCount=3
    )
    
    # Define message format
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    # Avoid adding multiple handlers if setup is called twice
    if not logger.handlers:
        logger.addHandler(handler)
        
    # Console output for debugging
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger