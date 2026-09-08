import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "click_interval": 0.1,
    "mouse_button": "left",
    "hotkey": "f8",
    "click_count": 0,
    "double_click": False,
    "random_jitter": 0.02
}


def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Load configuration from a JSON file, filling missing keys with defaults."""
    config = DEFAULT_CONFIG.copy()
    if not os.path.exists(filepath):
        save_config(config, filepath)
        return config

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            user_config = json.load(f)
            if isinstance(user_config, dict):
                config.update(user_config)
    except (json.JSONDecodeError, OSError):
        # Return default config if file is corrupted or unreadable
        pass

    return config


def save_config(config: Dict[str, Any], filepath: str = "config.json") -> bool:
    """Save configuration dictionary to a JSON file."""
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
        return True
    except OSError:
        return False
