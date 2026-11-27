import json
import os
from typing import Dict, Any, Optional

def load_click_settings(filepath: str) -> Dict[str, Any]:
    """Loads autoclicker configuration from a local JSON file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "repeat": -1}
    
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_click_settings(filepath: str, data: Dict[str, Any]) -> bool:
    """Persists current click settings to disk safely."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_click_data(data: Dict[str, Any]) -> bool:
    """Checks for required keys in settings dictionary."""
    required = {"interval", "button", "repeat"}
    return all(key in data for key in required)

def sanitize_click_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Ensures interval is positive and within bounds."""
    sanitized = data.copy()
    sanitized['interval'] = max(0.01, min(sanitized.get('interval', 0.1), 60.0))
    return sanitized