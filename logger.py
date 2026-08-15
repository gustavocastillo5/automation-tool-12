import logging

# Configure the logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ClickerLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_debug(self, message):
        self.logger.debug(message)

# Example usage:
if __name__ == '__main__':
    clicker_log = ClickerLogger('autoclicker')
    clicker_log.log_info('Autoclicker started')
    clicker_log.log_debug('This is a debug message')
    clicker_log.log_warning('This is a warning message')
    clicker_log.log_error('This is an error message')