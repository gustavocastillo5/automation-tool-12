import json
import os

DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "button": "left",
    "repeat_count": 100,
    "hotkey": "f9"
}

CONFIG_FILE = "config.json"

def load_configuration():
    """Loads configuration from disk or returns defaults."""
    if not os.path.exists(CONFIG_FILE):
        save_configuration(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    try:
        with open(CONFIG_FILE, "r") as f:
            user_config = json.load(f)
            # Merge with defaults to ensure missing keys are present
            return {**DEFAULT_CONFIG, **user_config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_configuration(config_data):
    """Persists current configuration to json file."""
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config_data, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")