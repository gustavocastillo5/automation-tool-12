import json
import os
from typing import Any, Dict

def load_clicker_config(filepath: str) -> Dict[str, Any]:
    """Load autoclicker configuration from a JSON file."""
    if not os.path.exists(filepath):
        return {
            "interval": 0.1,
            "button": "left",
            "repeat": 0
        }
    
    with open(filepath, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_clicker_config(filepath: str, data: Dict[str, Any]) -> None:
    """Persist current settings to the local filesystem."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def validate_click_interval(interval: float) -> float:
    """Ensure the click interval is within safe bounds."""
    min_interval = 0.01
    max_interval = 60.0
    return max(min_interval, min(interval, max_interval))

def format_click_stats(clicks: int, duration: float) -> str:
    """Return formatted string for performance logging."""
    cps = clicks / duration if duration > 0 else 0
    return f"Total Clicks: {clicks} | Average Rate: {cps:.2f} cps"