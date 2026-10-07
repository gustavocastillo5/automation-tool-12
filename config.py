import json
import os
from typing import Any, Dict

# Default configuration for the autoclicker
DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "max_clicks": 1000,
    "random_delay": False
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from file or returns defaults."""
    if not os.path.exists(filepath):
        return DEFAULT_CONFIG

    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            # Merge with defaults to ensure missing keys are handled
            return {**DEFAULT_CONFIG, **data}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """Persists current configuration to disk."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")