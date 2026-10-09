import json
import os

DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "button": "left",
    "repeat_limit": 1000,
    "hotkey": "f6"
}

def load_config(filepath: str) -> dict:
    """Load configuration from json file or return defaults."""
    if not os.path.exists(filepath):
        save_config(filepath, DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    try:
        with open(filepath, 'r') as f:
            user_config = json.load(f)
            # Merge user config with defaults to ensure keys exist
            return {**DEFAULT_CONFIG, **user_config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(filepath: str, config: dict) -> None:
    """Persist configuration to disk."""
    with open(filepath, 'w') as f:
        json.dump(config, f, indent=4)

# Instance for quick access in automation-tool-12
settings = load_config("settings.json")