import json
import os
from typing import Dict, Any

# Configuration defaults for autoclicker
DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": 0,
    "hotkey": "f6"
}

def load_session_data(filepath: str) -> Dict[str, Any]:
    """Reads click settings from local JSON file."""
    if not os.path.exists(filepath):
        return DEFAULT_CONFIG.copy()
    
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return {**DEFAULT_CONFIG, **data}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG.copy()

def save_session_data(filepath: str, data: Dict[str, Any]) -> bool:
    """Persists current clicker settings to disk."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

# Application constants
MAX_INTERVAL = 10.0
MIN_INTERVAL = 0.01
SUPPORTED_BUTTONS = ['left', 'right', 'middle']