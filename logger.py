import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str, log_file: str = 'automation.log') -> logging.Logger:
    """
    Configures a rotating file logger for the automation tool.
    Keeps logs at a manageable size of 1MB with 3 backups.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if logger is re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # File rotation setup
        handler = RotatingFileHandler(
            log_file, maxBytes=1024 * 1024, backupCount=3
        )
        handler.setFormatter(formatter)

        # Console output setup
        console = logging.StreamHandler()
        console.setFormatter(formatter)

        logger.addHandler(handler)
        logger.addHandler(console)

    return logger

# Global logger instance for the automation tool
logger = setup_logger('automation-tool-12')