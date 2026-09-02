import json
import os
from typing import List, Dict, Any

def load_click_data(filepath: str) -> List[Dict[str, Any]]:
    """Load autoclicker click data from JSON file.
    Returns empty list on errors or missing file.
    """
    if not os.path.isfile(filepath):
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, IOError, OSError):
        return []

def save_click_data(data: List[Dict[str, Any]], filepath: str) -> bool:
    """Save list of click dictionaries to JSON file.
    Creates parent directories if needed.
    """
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        return True
    except (IOError, OSError, TypeError):
        return False

def validate_click_entry(entry: Dict[str, Any]) -> bool:
    """Check if a single click entry has required fields."""
    if not isinstance(entry, dict):
        return False
    required = ['x', 'y']
    for key in required:
        if key not in entry:
            return False
        if not isinstance(entry[key], (int, float)):
            return False
    if 'delay_ms' in entry:
        if not isinstance(entry['delay_ms'], (int, float)) or entry['delay_ms'] < 0:
            return False
    if 'button' in entry:
        if entry['button'] not in ['left', 'right', 'middle']:
            return False
    return True

def filter_valid_clicks(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Return only valid click entries from the list."""
    return [entry for entry in data if validate_click_entry(entry)]

def get_click_statistics(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Compute basic statistics for the click sequence."""
    valid_data = filter_valid_clicks(data)
    if not valid_data:
        return {'count': 0, 'total_delay': 0, 'avg_delay': 0}
    delays = [d.get('delay_ms', 100) for d in valid_data]
    total_delay = sum(delays)
    avg_delay = total_delay / len(delays) if delays else 0
    return {
        'count': len(valid_data),
        'total_delay': total_delay,
        'avg_delay': round(avg_delay, 2),
        'min_delay': min(delays),
        'max_delay': max(delays)
    }

def merge_click_data(base: List[Dict[str, Any]], additions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Merge two click data lists after validation."""
    valid_base = filter_valid_clicks(base)
    valid_add = filter_valid_clicks(additions)
    return valid_base + valid_add