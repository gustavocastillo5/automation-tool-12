import json
import os

DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "hotkey": "f6",
    "repeat_count": 0,
    "randomization": False
}

def load_config(filepath="config.json"):
    """Loads configuration from disk or returns defaults."""
    if not os.path.exists(filepath):
        save_config(DEFAULT_CONFIG, filepath)
        return DEFAULT_CONFIG

    try:
        with open(filepath, "r") as f:
            config = json.load(f)
            # Merge with defaults to ensure missing keys are handled
            return {**DEFAULT_CONFIG, **config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config, filepath="config.json"):
    """Persists current configuration settings to disk."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")

# Initialization of global config
current_config = load_config()