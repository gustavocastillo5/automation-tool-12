import json
import os
from typing import List, Dict, Any

def load_click_data(filepath: str) -> List[Dict[str, Any]]:
    """Load autoclicker click data from JSON file.
    Returns empty list if file does not exist or is invalid.
    """
    if not os.path.isfile(filepath):
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        if isinstance(data, list):
            return data
        return []
    except (json.JSONDecodeError, IOError):
        return []

def save_click_data(data: List[Dict[str, Any]], filepath: str) -> bool:
    """Save autoclicker click data to JSON file.
    Returns True on success, False on failure.
    """
    try:
        directory = os.path.dirname(filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)
        return True
    except (IOError, OSError):
        return False

def validate_click_entry(entry: Dict[str, Any]) -> bool:
    """Check if a single click entry is valid."""
    if not isinstance(entry, dict):
        return False
    required_keys = {'x', 'y', 'interval'}
    if not required_keys.issubset(entry.keys()):
        return False
    try:
        x = int(entry['x'])
        y = int(entry['y'])
        interval = float(entry['interval'])
        if x < 0 or y < 0 or interval < 0:
            return False
        return True
    except (ValueError, TypeError):
        return False

def validate_click_data(data: List[Dict[str, Any]]) -> bool:
    """Validate entire list of click data."""
    if not isinstance(data, list):
        return False
    return all(validate_click_entry(entry) for entry in data)

def filter_valid_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Return only valid click entries from the data."""
    return [entry for entry in data if validate_click_entry(entry)]

def calculate_total_time(data: List[Dict[str, Any]]) -> float:
    """Calculate total time for the click sequence."""
    valid_data = filter_valid_data(data)
    return sum(float(entry.get('interval', 0)) for entry in valid_data)

def normalize_positions(data: List[Dict[str, Any]], offset_x: int = 0, offset_y: int = 0) -> List[Dict[str, Any]]:
    """Shift all positions by the given x and y offsets."""
    normalized = []
    for entry in data:
        if validate_click_entry(entry):
            new_entry = entry.copy()
            new_entry['x'] = int(new_entry['x']) + offset_x
            new_entry['y'] = int(new_entry['y']) + offset_y
            normalized.append(new_entry)
    return normalized