import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "max_clicks": 1000,
    "hotkey": "f6"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from JSON or returns defaults."""
    if not os.path.exists(filepath):
        return DEFAULT_CONFIG.copy()
    
    try:
        with open(filepath, "r") as f:
            user_config = json.load(f)
            # Merge user config with defaults
            config = DEFAULT_CONFIG.copy()
            config.update(user_config)
            return config
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG.copy()

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """Persists current configuration to JSON file."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")