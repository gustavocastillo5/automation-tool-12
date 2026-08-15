import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=5 * 1024 * 1024, backup_count=3):
    logger = logging.getLogger('AutoClickerLogger')
    logger.setLevel(logging.DEBUG)

    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)
    return logger

# Example usage: logger = setup_logger()
logger = setup_logger()  # Uncomment to use