import re

def validate_coordinate(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """Checks if coordinates are within screen boundaries."""
    return 0 <= x < screen_width and 0 <= y < screen_height

def validate_interval(interval: float) -> bool:
    """Ensures click interval is within safe operational limits."""
    return 0.01 <= interval <= 60.0

def validate_key_string(key: str) -> bool:
    """Validates that a key input string is non-empty and simple."""
    return bool(re.match(r'^[a-zA-Z0-9]+$', key))

def validate_click_count(count: int) -> bool:
    """Checks for positive click iteration counts."""
    return count > 0 or count == -1

def sanitize_config(data: dict) -> dict:
    """Filters out invalid entries from configuration dictionary."""
    sanitized = {}
    for key, value in data.items():
        if value is not None:
            sanitized[key] = value
    return sanitized