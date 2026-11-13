import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "click_interval": 0.1,
    "mouse_button": "left",
    "hotkey": "f6",
    "max_clicks": 0,
    "random_jitter": 0.02,
    "start_delay": 3.0,
}


def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Load configuration from a JSON file, creating it with defaults if missing."""
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(config_path):
        try:
            with open(config_path, "w", encoding="utf-8") as f:
                json.dump(config, f, indent=4)
        except IOError:
            pass
        return config

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            user_config = json.load(f)
            if isinstance(user_config, dict):
                config.update(user_config)
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

    return config


def save_config(config: Dict[str, Any], config_path: str = "config.json") -> bool:
    """Save the given configuration parameters back to file."""
    try:
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
        return True
    except IOError:
        return False
