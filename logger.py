import logging
import os
import sys

def setup_logger(name: str = 'automation-tool-12') -> logging.Logger:
    """Initializes application logger with safe file handling."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    try:
        log_dir = 'logs'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
            
        file_handler = logging.FileHandler(os.path.join(log_dir, 'automation.log'))
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except (OSError, PermissionError) as e:
        # Fallback to console if file logging fails due to system permissions
        console_handler = logging.StreamHandler(sys.stderr)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        logger.error(f"Logging file initialization failed: {e}. Falling back to stderr.")

    return logger

def log_exception(logger: logging.Logger, error: Exception) -> None:
    """Standardized exception formatting for autoclicker crashes."""
    if isinstance(error, (KeyboardInterrupt, SystemExit)):
        return
    
    logger.error(f"Unhandled exception type {type(error).__name__}: {str(error)}", exc_info=True)