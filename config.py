import os

# Configuration settings for automation-tool-12

class AppConfig:
    # Core execution settings
    DEFAULT_INTERVAL = 0.1
    MAX_CLICK_LIMIT = 1000
    
    # Logging configuration
    LOG_FILE = "automation.log"
    LOG_LEVEL = "INFO"

    # Path management for internal assets
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, "data")

    @classmethod
    def get_settings(cls):
        """Returns a dictionary of all configurable parameters."""
        return {
            "interval": cls.DEFAULT_INTERVAL,
            "max_limit": cls.MAX_CLICK_LIMIT,
            "log_level": cls.LOG_LEVEL
        }

def validate_config(config_dict):
    """Ensures basic constraints on application settings."""
    if config_dict.get("interval", 0) < 0:
        raise ValueError("Interval cannot be negative")
    return True