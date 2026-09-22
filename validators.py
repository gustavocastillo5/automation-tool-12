import re
from typing import Any, Optional

def validate_interval(interval: Any) -> float:
    """Ensures click interval is a positive float."""
    try:
        value = float(interval)
        if value < 0.001:
            return 0.001
        return value
    except (ValueError, TypeError):
        return 0.1

def validate_coordinates(x: Any, y: Any) -> tuple[int, int]:
    """Sanitizes coordinate inputs to integer values."""
    try:
        return int(x), int(y)
    except (ValueError, TypeError):
        return 0, 0

def is_valid_hotkey(key: str) -> bool:
    """Checks if provided key follows simple single-char format."""
    pattern = r'^[a-z0-9]$'
    return bool(re.match(pattern, str(key).lower()))

def sanitize_config_dict(config: dict) -> dict:
    """Cleans dictionary values for core execution logic."""
    return {
        "interval": validate_interval(config.get("interval")),
        "coords": validate_coordinates(
            config.get("x", 0),
            config.get("y", 0)
        ),
        "hotkey": config.get("hotkey", "f1")
    }