import logging
from logging.handlers import RotatingFileHandler

# Set up logger configuration
def setup_logger(log_file='app.log', max_bytes=5 * 1024 * 1024, backup_count=5):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)
    return logger

# Example usage
if __name__ == '__main__':
    log = setup_logger()
    log.info('Logger is set up!')
    log.warning('This is a warning message.')
    log.error('This is an error message.')
