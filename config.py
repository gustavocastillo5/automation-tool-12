import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "hotkey": "f6",
    "repeat": True
}

def load_config(filepath: str = "settings.json") -> Dict[str, Any]:
    """Loads user settings from a JSON file."""
    if not os.path.exists(filepath):
        save_config(DEFAULT_CONFIG, filepath)
        return DEFAULT_CONFIG
    
    try:
        with open(filepath, "r") as f:
            return {**DEFAULT_CONFIG, **json.load(f)}
    except (IOError, ValueError):
        return DEFAULT_CONFIG

def save_config(config: Dict[str, Any], filepath: str = "settings.json") -> None:
    """Persists current configuration state to disk."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Config save failure: {e}")