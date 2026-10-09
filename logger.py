import logging
import os
import sys
from logging.handlers import RotatingFileHandler

class SafeLogger:
    """
    Thread-safe logger for the autoclicker tool with fallback error handling
    for permission issues, missing directories, and full disks.
    """
    def __init__(self, name: str = 'autoclicker', log_file: str = 'logs/app.log'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.logger.handlers.clear()  # Prevent duplicate handlers across instances

        # Standard console handler (always safe fallback)
        console_formatter = logging.Formatter('[%(levelname)s] %(asctime)s - %(message)s')
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(console_formatter)
        console_handler.setLevel(logging.INFO)
        self.logger.addHandler(console_handler)

        # Attempt to set up rotating file handler with robust edge-case handling
        try:
            log_dir = os.path.dirname(log_file)
            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir, exist_ok=True)

            # Rotating file handler prevents filling up the disk
            file_handler = RotatingFileHandler(
                log_file, maxBytes=1024 * 1024, backupCount=3, encoding='utf-8'
            )
            file_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s')
            file_handler.setFormatter(file_formatter)
            file_handler.setLevel(logging.DEBUG)
            self.logger.addHandler(file_handler)
        except (OSError, PermissionError) as e:
            # Gracefully fall back to console logging if directories are read-only or full
            self.logger.warning(
                f'File logging disabled. Failed to initialize log file at {log_file} due to: {e}'
            )

    def get_logger(self) -> logging.Logger:
        return self.logger
