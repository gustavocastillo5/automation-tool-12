import json
import os
from typing import Any, Dict

def load_click_config(filepath: str) -> Dict[str, Any]:
    """Reads and parses clicker settings from JSON file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "repeats": 0}
    
    with open(filepath, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_click_config(filepath: str, data: Dict[str, Any]) -> bool:
    """Persists current clicker configuration to local storage."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError):
        return False

def validate_coordinates(coords: tuple) -> bool:
    """Ensures screen coordinates are within valid bounds."""
    x, y = coords
    return isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0

def format_click_stats(count: int, duration: float) -> str:
    """Generates human readable string for UI display."""
    cps = count / duration if duration > 0 else 0
    return f"Clicks: {count} | Avg Speed: {cps:.2f} cps"