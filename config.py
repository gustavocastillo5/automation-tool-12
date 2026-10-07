import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "hotkey": "f8",
    "repeat_count": 0,
    "mouse_button": "left"
}

CONFIG_FILE = "settings.json"

def load_config() -> Dict[str, Any]:
    """Loads configuration from JSON file with defaults."""
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    try:
        with open(CONFIG_FILE, "r") as f:
            user_config = json.load(f)
            # Merge with defaults to ensure missing keys are handled
            config = DEFAULT_CONFIG.copy()
            config.update(user_config)
            return config
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config: Dict[str, Any]) -> None:
    """Saves current configuration to JSON file."""
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")

# Initialize global settings
settings = load_config()