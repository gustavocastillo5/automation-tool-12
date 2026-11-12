import json
import os
from typing import Dict, Any, Optional

def load_click_data(filepath: str) -> Dict[str, Any]:
    """Loads autoclicker configuration settings from local json."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "repeats": 1}
    
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_click_data(filepath: str, data: Dict[str, Any]) -> bool:
    """Persists current clicker configuration to storage file."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_click_settings(data: Dict[str, Any]) -> bool:
    """Checks validity of autoclicker coordinate and timing."""
    required = {'interval', 'button'}
    if not all(k in data for k in required):
        return False
    return isinstance(data['interval'], (int, float)) and data['interval'] > 0

def sanitize_coordinates(raw_data: Dict[str, Any]) -> Dict[str, int]:
    """Ensures click coordinates are positive integers."""
    return {
        "x": max(0, int(raw_data.get("x", 0))),
        "y": max(0, int(raw_data.get("y", 0)))
    }