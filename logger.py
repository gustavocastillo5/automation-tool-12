import logging
import sys
from typing import Optional

class Logger:
    """Handles application-wide logging for automation-tool-12."""

    def __init__(self, name: str = "autoclicker", level: int = logging.INFO) -> None:
        """Initializes the logger instance with standard formatting."""
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        """Logs an informational message to the console."""
        self.logger.info(message)

    def error(self, message: str, exc_info: Optional[bool] = False) -> None:
        """Logs an error message with optional traceback inclusion."""
        self.logger.error(message, exc_info=exc_info)

    def warning(self, message: str) -> None:
        """Logs a warning message to the console."""
        self.logger.warning(message)