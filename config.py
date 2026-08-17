import logging
from logging.handlers import RotatingFileHandler

# Logger configuration
LOG_FILE = 'app.log'
LOG_MAX_BYTES = 5 * 1024 * 1024  # 5 MB
LOG_BACKUP_COUNT = 3

# Setup logger function

def setup_logger():
    logger = logging.getLogger('AutoClickerLogger')
    logger.setLevel(logging.DEBUG)  # Set to DEBUG level for full verbosity

    # Create a rotating file handler
    handler = RotatingFileHandler(LOG_FILE, maxBytes=LOG_MAX_BYTES, backupCount=LOG_BACKUP_COUNT)
    handler.setLevel(logging.DEBUG)

    # Create formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)
    return logger

# Initialize the logger
logger = setup_logger()