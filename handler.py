import json
import os
from typing import Dict, Any

def load_click_settings(filepath: str) -> Dict[str, Any]:
    """Load autoclicker configuration from a JSON file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "enabled": False}
    
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {"interval": 0.1, "button": "left", "enabled": False}

def save_click_settings(filepath: str, data: Dict[str, Any]) -> bool:
    """Persist autoclicker configuration to disk."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_click_data(data: Dict[str, Any]) -> bool:
    """Verify data integrity for clicker operations."""
    required = ["interval", "button", "enabled"]
    return all(key in data for key in required) and isinstance(data["interval"], (int, float))