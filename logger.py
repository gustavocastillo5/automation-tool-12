import logging
import sys
from logging.handlers import RotatingFileHandler

# Configure performance-optimized logging for high-frequency events
class PerformanceLogger:
    def __init__(self, name="automation-tool-12", level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        # Use memory-efficient formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
        # Rotating file handler to prevent disk I/O bottlenecks
        file_handler = RotatingFileHandler(
            "app.log", maxBytes=1024*1024*5, backupCount=3
        )
        file_handler.setFormatter(formatter)
        
        # Stream handler for console debugging
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

    def get_logger(self):
        return self.logger

# Singleton pattern for consistent logging performance
_logger_instance = PerformanceLogger().get_logger()

def get_logger():
    return _logger_instance