import json
import os
from typing import Dict, Any

def load_click_profile(filepath: str) -> Dict[str, Any]:
    """Loads autoclicker settings from a JSON file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "iterations": 0}
    
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_click_profile(filepath: str, data: Dict[str, Any]) -> bool:
    """Persists autoclicker configuration to disk."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_profile(data: Dict[str, Any]) -> bool:
    """Verifies structure of configuration dictionary."""
    required_keys = {"interval", "button", "iterations"}
    return all(key in data for key in required_keys)

def get_default_config() -> Dict[str, Any]:
    """Returns base template for new profiles."""
    return {
        "interval": 0.5,
        "button": "left",
        "iterations": 100,
        "randomization": False
    }