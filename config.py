import json
import os

DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "button": "left",
    "hotkey": "f6",
    "repeat_count": 0
}

def load_config(filepath="settings.json"):
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

def save_config(config, filepath="settings.json"):
    """Persists configuration dictionary to a JSON file."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")

# Initialize global configuration state
app_config = load_config()