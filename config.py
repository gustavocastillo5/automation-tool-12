import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": 100
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Reads configuration from a local JSON file."""
    if not os.path.exists(filepath):
        return DEFAULT_CONFIG
    
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> bool:
    """Persists current automation settings to disk."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
        return True
    except IOError:
        return False

def validate_interval(interval: float) -> float:
    """Ensures click interval is within safe bounds."""
    return max(0.01, min(interval, 60.0))