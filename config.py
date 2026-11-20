import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": 0,
    "hotkey": "f6"
}

def load_settings(filepath: str = "settings.json") -> Dict[str, Any]:
    """Load autoclicker configuration from JSON file."""
    if not os.path.exists(filepath):
        save_settings(DEFAULT_CONFIG, filepath)
        return DEFAULT_CONFIG
    
    try:
        with open(filepath, "r") as f:
            return {**DEFAULT_CONFIG, **json.load(f)}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_settings(data: Dict[str, Any], filepath: str = "settings.json") -> bool:
    """Persist current autoclicker settings to disk."""
    try:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_interval(interval: float) -> float:
    """Ensure click interval is within safe bounds."""
    return max(0.01, min(interval, 60.0))
