import json
import os

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": 0,
    "hotkey": "f6"
}

CONFIG_FILE = "settings.json"

def load_config():
    """load settings from file or return defaults"""
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    try:
        with open(CONFIG_FILE, "r") as f:
            user_config = json.load(f)
            # ensure all keys exist
            return {**DEFAULT_CONFIG, **user_config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config_data):
    """persist current settings to json"""
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config_data, f, indent=4)
    except IOError as e:
        print(f"failed to save config: {e}")

# initialized state for the application
active_config = load_config()