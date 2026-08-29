import logging
import json
import os
from datetime import datetime

def configure_autoclicker_logger(log_level="INFO", log_file="autoclicker.log"):
    """Set up logging for the autoclicker application."""
    logger = logging.getLogger("autoclicker")
    logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
    return logger

class AutoclickerDataLogger:
    """Utility class for autoclicker data handling and logging."""
    def __init__(self, data_file="click_data.json"):
        self.data_file = data_file
        self.logger = configure_autoclicker_logger()
        if not os.path.exists(self.data_file):
            with open(self.data_file, "w") as f:
                json.dump([], f)

    def log_click(self, x, y, interval, button="left"):
        """Log click position, interval and button."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "x": x,
            "y": y,
            "interval": interval,
            "button": button
        }
        try:
            with open(self.data_file, "r+") as f:
                data = json.load(f)
                data.append(entry)
                f.seek(0)
                json.dump(data, f, indent=2)
                f.truncate()
            self.logger.info(f"Logged click at {x},{y}")
        except Exception as e:
            self.logger.error(f"Log error: {e}")

    def get_data(self):
        """Return all logged click data."""
        try:
            with open(self.data_file, "r") as f:
                return json.load(f)
        except Exception as e:
            self.logger.error(f"Read error: {e}")
            return []

    def clear_data(self):
        """Clear all logged data."""
        try:
            with open(self.data_file, "w") as f:
                json.dump([], f)
            self.logger.info("Data cleared")
        except Exception as e:
            self.logger.error(f"Clear error: {e}")
