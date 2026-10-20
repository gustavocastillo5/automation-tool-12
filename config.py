import json
import os

DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "button": "left",
    "hotkey": "f6",
    "repeat_count": 0
}

def load_config(filepath: str) -> dict:
    """
    loads configuration from json file with defaults fallback
    """
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r') as f:
                user_data = json.load(f)
                config.update(user_data)
        except (json.JSONDecodeError, IOError):
            pass
            
    return config

def save_config(filepath: str, config: dict) -> bool:
    """
    persists current configuration to disk
    """
    try:
        with open(filepath, 'w') as f:
            json.dump(config, f, indent=4)
        return True
    except IOError:
        return False