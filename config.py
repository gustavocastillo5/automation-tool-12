import json
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "cps": 10.0,
    "mouse_button": "left",
    "hotkey": "f6",
    "click_limit": 0,
    "random_interval": False,
    "interval_jitter": 0.02,
}


def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Load configuration from JSON file, merging missing values with defaults."""
    path = Path(config_path)
    config = DEFAULT_CONFIG.copy()

    if not path.exists():
        save_config(config, config_path)
        return config

    try:
        with open(path, "r", encoding="utf-8") as f:
            user_config = json.load(f)
            if isinstance(user_config, dict):
                config.update(user_config)
    except (json.JSONDecodeError, OSError):
        # Fallback to default configuration if file read fails
        pass

    return config


def save_config(config: Dict[str, Any], config_path: str = "config.json") -> None:
    """Save configuration dictionary to a JSON file."""
    path = Path(config_path)
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
    except OSError:
        pass
