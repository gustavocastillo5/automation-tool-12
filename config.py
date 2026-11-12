import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "interval_ms": 100,
    "button": "left",
    "repeat_count": 0,
    "hotkey": "f6"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Load configuration from JSON file or return defaults."""
    if not os.path.exists(filepath):
        return DEFAULT_CONFIG.copy()

    try:
        with open(filepath, "r") as f:
            user_config = json.load(f)
            config = DEFAULT_CONFIG.copy()
            config.update(user_config)
            return config
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG.copy()

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """Persist current configuration to a JSON file."""
    with open(filepath, "w") as f:
        json.dump(config, f, indent=4)