import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "button": "left",
    "repeat": -1,
    "hotkey": "f8"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from JSON file or returns default."""
    if not os.path.exists(filepath):
        return DEFAULT_CONFIG.copy()

    try:
        with open(filepath, "r") as f:
            user_config = json.load(f)
            # Merge with defaults to ensure missing keys are filled
            config = DEFAULT_CONFIG.copy()
            config.update(user_config)
            return config
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG.copy()

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """Persists current configuration to JSON file."""
    with open(filepath, "w") as f:
        json.dump(config, f, indent=4)