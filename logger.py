import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='automation-tool-12', log_file='app.log', level=logging.INFO):
    """Initializes a rotating file logger for the application."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if function is called multiple times
    if not logger.handlers:
        # Ensure logs directory exists
        os.makedirs('logs', exist_ok=True)
        log_path = os.path.join('logs', log_file)

        # Create rotating handler: 5MB per file, keep 3 backup files
        handler = RotatingFileHandler(
            log_path, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        
        # Formatting
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        
        # Also output to console for real-time monitoring
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger