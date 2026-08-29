"""Validators for automation-tool-12 autoclicker."""

import re
from typing import Tuple, Union

def validate_coordinates(x: Union[int, float], y: Union[int, float], max_x: int = 1920, max_y: int = 1080) -> bool:
    """Validate if x and y are within screen dimensions."""
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return False
    # Ensure non-negative and within bounds
    return 0 <= x <= max_x and 0 <= y <= max_y

def validate_interval(seconds: float) -> bool:
    """Validate click interval is between 0.01 and 3600 seconds."""
    if not isinstance(seconds, (int, float)):
        return False
    return 0.01 <= seconds <= 3600

def validate_hotkey(hotkey: str) -> bool:
    """Validate hotkey format like 'ctrl+shift+a'."""
    if not isinstance(hotkey, str) or not hotkey.strip():
        return False
    # Split by + and check parts
    parts = [p.strip().lower() for p in hotkey.split('+') if p.strip()]
    if not parts:
        return False
    modifiers = {'ctrl', 'alt', 'shift', 'win', 'cmd'}
    # Simple key validation
    for part in parts:
        if part in modifiers:
            continue
        if not re.match(r'^[a-z0-9]+$', part) and not re.match(r'^f\d+$', part):
            return False
    return True

def validate_click_count(count: int) -> bool:
    """Validate number of clicks is positive and reasonable."""
    if not isinstance(count, int):
        return False
    return 1 <= count <= 100000

def validate_screen_region(region: Tuple[int, int, int, int]) -> bool:
    """Validate a screen region tuple (x, y, width, height)."""
    if not isinstance(region, tuple) or len(region) != 4:
        return False
    return all(isinstance(val, int) and val >= 0 for val in region)

def validate_click_points(points: list) -> bool:
    """Validate a list of (x, y) click points."""
    if not isinstance(points, list) or len(points) == 0:
        return False
    for point in points:
        if not isinstance(point, (list, tuple)) or len(point) != 2:
            return False
        x, y = point
        if not validate_coordinates(x, y):
            return False
    return True