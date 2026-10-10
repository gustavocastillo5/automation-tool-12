import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='automation-tool', log_file='automation.log'):
    """Initializes a rotating file logger for the application."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if logger is re-initialized
    if logger.handlers:
        return logger

    # Rotate at 1MB, keeping up to 3 backup files
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=1*1024*1024, 
        backupCount=3
    )
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    
    # Console output for real-time monitoring
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger