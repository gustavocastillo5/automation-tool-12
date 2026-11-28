import logging
import sys
from logging.handlers import RotatingFileHandler

# Configure performance-optimized logging for high-frequency events
# Using buffer size to reduce disk I/O overhead

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOG_FILE = 'automation.log'

def setup_logger(name: str = 'autoclicker_logger'):
    """Initialize optimized logger instance"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        # Rotating handler to prevent unbounded log growth
        handler = RotatingFileHandler(
            LOG_FILE, 
            maxBytes=1024 * 1024 * 5, 
            backupCount=3
        )
        
        # Use memory buffering to improve click throughput
        formatter = logging.Formatter(LOG_FORMAT)
        handler.setFormatter(formatter)
        
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.addHandler(stream_handler)

    return logger

# Instantiate singleton for core modules
app_logger = setup_logger()