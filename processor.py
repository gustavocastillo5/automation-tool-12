import json
import os
from typing import Dict, List, Optional

def load_click_profile(filepath: str) -> Dict:
    """Loads autoclicker configuration settings from a JSON file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "repeat": False}
    
    with open(filepath, 'r') as file:
        return json.load(file)

def save_click_profile(filepath: str, data: Dict) -> bool:
    """Persists current autoclicker state to disk."""
    try:
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
        return True
    except (IOError, TypeError):
        return False

def validate_coordinates(coords: List[int]) -> bool:
    """Ensures x and y screen coordinates are within bounds."""
    return len(coords) == 2 and all(isinstance(c, int) and c >= 0 for c in coords)

def format_click_log(action: str, coords: List[int]) -> str:
    """Creates formatted log strings for click events."""
    x, y = coords
    return f"[{action.upper()}] event at location: {x}, {y}"