import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "button": "left",
    "max_clicks": 1000,
    "auto_start": False
}

def load_configuration(filepath: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from a JSON file with fallback to defaults.
    """
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load config {filepath}: {e}. Using defaults.")
            
    return config

def save_configuration(config: Dict[str, Any], filepath: str = "config.json") -> bool:
    """
    Persists the current configuration dictionary to a JSON file.
    """
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
        return True
    except IOError as e:
        print(f"Error saving config to {filepath}: {e}")
        return False