import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": 0,
    "hotkey": "f6"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from disk or returns defaults if missing
    """
    if not os.path.exists(filepath):
        save_default_config(filepath)
        return DEFAULT_CONFIG

    try:
        with open(filepath, "r") as f:
            config = json.load(f)
            # Merge with defaults to ensure missing keys are present
            return {**DEFAULT_CONFIG, **config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_default_config(filepath: str) -> None:
    """
    Persists default configuration to specified file
    """
    try:
        with open(filepath, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
    except IOError as e:
        print(f"Failed to write config: {e}")