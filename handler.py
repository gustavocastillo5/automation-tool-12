import json
import os

def save_click_profile(profile_name, data):
    """Persist autoclicker configuration to local json file."""
    file_path = f"profiles/{profile_name}.json"
    os.makedirs("profiles", exist_ok=True)
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError) as e:
        print(f"Storage error: {e}")
        return False

def load_click_profile(profile_name):
    """Load existing click pattern from storage."""
    file_path = f"profiles/{profile_name}.json"
    if not os.path.exists(file_path):
        return None
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return None

def validate_coordinates(coords):
    """Check if click coordinates are valid integers."""
    if not isinstance(coords, dict):
        return False
    return all(isinstance(coords.get(k), int) for k in ('x', 'y'))