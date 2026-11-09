import json
import os
import re
from typing import Dict, List, Optional

def parse_interval_to_seconds(interval_str: str) -> float:
    """Convert human-readable time string (e.g., '500ms', '1.5s', '2m') to seconds."""
    match = re.match(r"^(\d+(?:\.\d+)?)\s*(ms|s|m|h)?$", interval_str.strip().lower())
    if not match:
        raise ValueError(f"Invalid interval format: {interval_str}")
    
    value, unit = float(match.group(1)), match.group(2) or "s"
    
    if unit == "ms":
        return value / 1000.0
    elif unit == "s":
        return value
    elif unit == "m":
        return value * 60.0
    elif unit == "h":
        return value * 3600.0
    return value

def load_click_profile(filepath: str) -> List[Dict[str, float]]:
    """Load click sequence profiles from a JSON file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Profile file not found: {filepath}")
    
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    if not isinstance(data, list):
        raise ValueError("Profile file must contain a JSON array of click actions")
        
    return data

def save_click_profile(filepath: str, click_data: List[Dict[str, float]]) -> bool:
    """Save click sequence data safely to a JSON profile file."""
    try:
        dirname = os.path.dirname(filepath)
        if dirname:
            os.makedirs(dirname, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(click_data, f, indent=4)
        return True
    except Exception:
        return False
