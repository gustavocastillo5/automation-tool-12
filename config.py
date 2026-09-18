import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": -1,
    "hotkey": "f6"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from JSON file or returns defaults.
    """
    if not os.path.exists(filepath):
        return DEFAULT_CONFIG.copy()

    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            # Merge loaded data with defaults to ensure all keys exist
            config = DEFAULT_CONFIG.copy()
            config.update(data)
            return config
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG.copy()

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """
    Persists configuration to disk.
    """
    with open(filepath, "w") as f:
        json.dump(config, f, indent=4)