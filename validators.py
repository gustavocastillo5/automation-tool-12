import re

def validate_coordinates(x: int, y: int) -> bool:
    """Ensures screen coordinates are within valid range."""
    return isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0

def validate_interval(interval: float) -> bool:
    """Checks if click interval is within safe bounds."""
    return isinstance(interval, (int, float)) and 0.01 <= interval <= 60.0

def validate_hotkey(key: str) -> bool:
    """Validates hotkey string format for the automation trigger."""
    pattern = r'^[a-zA-Z0-9+]+$'
    return bool(re.match(pattern, key))