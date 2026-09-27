import json
import os

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "hotkey": "f6",
    "repeat_count": 0
}

def load_config(filepath="settings.json"):
    """Loads configuration from a JSON file or returns defaults."""
    if not os.path.exists(filepath):
        return DEFAULT_CONFIG
    
    try:
        with open(filepath, "r") as f:
            return {**DEFAULT_CONFIG, **json.load(f)}
    except (IOError, ValueError):
        return DEFAULT_CONFIG

def save_config(config, filepath="settings.json"):
    """Persists current configuration state to disk."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")

if __name__ == "__main__":
    # Demo loading
    current_cfg = load_config()
    print(f"Active configuration: {current_cfg}")