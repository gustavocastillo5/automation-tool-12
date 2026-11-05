import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = "automation_tool") -> logging.Logger:
    """
    Configures a rotating file logger for automation-tool-12.
    Limits file size to 1MB and keeps 3 backups.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if re-initialized
    if logger.hasHandlers():
        logger.handlers.clear()

    log_directory = "logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    log_file = os.path.join(log_directory, f"{name}.log")
    
    # Create rotating file handler
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=1_048_576, 
        backupCount=3
    )
    
    # Set format: timestamp - name - level - message
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    
    # Console output for visibility during development
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger