import json
import os
from typing import Any, Dict

def load_click_config(filepath: str) -> Dict[str, Any]:
    """Loads autoclicker settings from a JSON file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "repeat": 0}
    
    with open(filepath, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_click_config(filepath: str, data: Dict[str, Any]) -> None:
    """Saves autoclicker settings to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def validate_coordinates(coords: Dict[str, int]) -> bool:
    """Ensures x and y coordinates are positive integers."""
    return all(isinstance(v, int) and v >= 0 for v in coords.values())

def format_log_entry(action: str, status: str) -> str:
    """Creates a formatted string for tool logging."""
    return f"[ACTION: {action.upper()}] Status: {status}"