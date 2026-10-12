import json
import os

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "hotkey": "f6",
    "repeat": True
}

def load_config(filepath: str = "config.json") -> dict:
    """Loads configuration from disk or returns defaults if missing."""
    if not os.path.exists(filepath):
        save_config(DEFAULT_CONFIG, filepath)
        return DEFAULT_CONFIG
    
    try:
        with open(filepath, "r") as f:
            config = json.load(f)
            return {**DEFAULT_CONFIG, **config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config: dict, filepath: str = "config.json") -> None:
    """Persists current configuration state to local file."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")