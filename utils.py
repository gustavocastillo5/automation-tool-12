import json
import os
from typing import Any, Dict

def load_click_config(filepath: str) -> Dict[str, Any]:
    """Loads configuration from a JSON file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "repeat": 1}
    
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_click_config(filepath: str, data: Dict[str, Any]) -> bool:
    """Persists autoclicker configuration to disk."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_coordinates(x: int, y: int) -> bool:
    """Checks if coordinates are non-negative integers."""
    return isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0

def format_log_entry(action: str, status: str) -> str:
    """Creates a standard log message format."""
    return f"[AUTOCLICKER] {action.upper()}: {status}"