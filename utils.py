import json
import os
from typing import Dict, Any

CONFIG_FILE = "autoclicker_config.json"

def load_click_data() -> Dict[str, Any]:
    """Load autoclicker configuration from local storage."""
    if not os.path.exists(CONFIG_FILE):
        return {"interval": 0.1, "button": "left", "enabled": False}
    
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_click_data(data: Dict[str, Any]) -> bool:
    """Persist autoclicker configuration to local storage."""
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_interval(interval: float) -> bool:
    """Ensure click interval remains within safe bounds."""
    return 0.01 <= interval <= 60.0

def format_coords(x: int, y: int) -> str:
    """Format screen coordinates for logging."""
    return f"({x}, {y})"