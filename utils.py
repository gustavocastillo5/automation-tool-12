import json
import os

def load_click_config(filepath: str) -> dict:
    """Loads autoclicker settings from a JSON file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "repeat": False}
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_click_config(filepath: str, data: dict) -> bool:
    """Persists autoclicker settings to disk."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_click_params(config: dict) -> bool:
    """Ensures configuration values are within safe bounds."""
    interval = config.get("interval", 0.0)
    if not isinstance(interval, (int, float)) or interval < 0.01:
        return False
    if config.get("button") not in ["left", "right", "middle"]:
        return False
    return True