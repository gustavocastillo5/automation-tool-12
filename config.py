import json
import os

# default configuration for autoclicker operations
DEFAULT_CONFIG = {
    "interval_seconds": 0.1,
    "click_button": "left",
    "max_clicks": 1000,
    "hotkey": "f8"
}

def load_config(filepath: str) -> dict:
    """loads configuration from json file or returns defaults"""
    if not os.path.exists(filepath):
        return DEFAULT_CONFIG

    try:
        with open(filepath, 'r') as f:
            user_config = json.load(f)
            # merge user settings into defaults
            config = DEFAULT_CONFIG.copy()
            config.update(user_config)
            return config
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(filepath: str, config: dict) -> None:
    """persists current configuration to json file"""
    with open(filepath, 'w') as f:
        json.dump(config, f, indent=4)