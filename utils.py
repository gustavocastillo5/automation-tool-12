import json
import os
from typing import Dict, Any

def load_click_config(file_path: str) -> Dict[str, Any]:
    """Loads autoclicker parameters from a local JSON file."""
    if not os.path.exists(file_path):
        return {"interval": 0.1, "button": "left", "repeats": 100}
    
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error reading config: {e}")
        return {}

def save_click_config(file_path: str, data: Dict[str, Any]) -> bool:
    """Persists autoclicker state to disk for future runs."""
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError as e:
        print(f"Error saving config: {e}")
        return False

def validate_coordinates(x: int, y: int) -> bool:
    """Ensures screen coordinates are within valid range."""
    return isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0

def format_click_stats(clicks: int, duration: float) -> str:
    """Calculates and formats simple performance metrics."""
    cps = clicks / duration if duration > 0 else 0
    return f"Total Clicks: {clicks} | Average Speed: {cps:.2f} CPS"