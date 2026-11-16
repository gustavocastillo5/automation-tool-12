import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = 'automation-tool-12', log_file: str = 'app.log') -> logging.Logger:
    """
    Configures a rotating file logger for the autoclicker.
    Limits file size to 1MB and keeps 3 backup files.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if function is called multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotate logs: 1MB per file, 3 backups
        file_handler = RotatingFileHandler(
            log_file, maxBytes=1024*1024, backupCount=3
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Optional: output to console as well
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Instantiate default logger instance for global usage
app_logger = setup_logger()