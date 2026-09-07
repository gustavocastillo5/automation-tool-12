"""Validation utilities for autoclicker configuration and parameters."""

from typing import Dict, Any, Tuple


class ValidationError(Exception):
    """Custom exception raised when input validation fails."""
    pass


def validate_click_interval(interval: float) -> float:
    """Ensure click interval is positive and within acceptable bounds."""
    if not isinstance(interval, (int, float)):
        raise ValidationError(f"Interval must be a number, got {type(interval).__name__}")
    if interval < 0.001:
        raise ValidationError("Interval must be at least 0.001 seconds (1ms)")
    if interval > 3600:
        raise ValidationError("Interval cannot exceed 3600 seconds (1 hour)")
    return float(interval)


def validate_coordinates(coords: Tuple[int, int], screen_size: Tuple[int, int]) -> Tuple[int, int]:
    """Validate click coordinates against target screen boundaries."""
    if not isinstance(coords, (tuple, list)) or len(coords) != 2:
        raise ValidationError("Coordinates must be a tuple of (x, y)")
    
    x, y = coords
    if not (isinstance(x, int) and isinstance(y, int)):
        raise ValidationError("Coordinate values must be integers")
    
    max_x, max_y = screen_size
    if x < 0 or x > max_x or y < 0 or y > max_y:
        raise ValidationError(f"Coordinates ({x}, {y}) out of screen bounds ({max_x}x{max_y})")
    
    return int(x), int(y)


def validate_click_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """Validate entire click configuration before execution loop."""
    required_keys = {"interval", "click_type", "repeat_count"}
    missing = required_keys - set(config.keys())
    if missing:
        raise ValidationError(f"Missing required config fields: {', '.join(missing)}")
    
    valid_types = {"left", "right", "middle", "double"}
    if config["click_type"] not in valid_types:
        raise ValidationError(f"Invalid click_type '{config['click_type']}'. Must be one of {valid_types}")
    
    repeat = config["repeat_count"]
    if not isinstance(repeat, int) or repeat < 0:
        raise ValidationError("repeat_count must be a non-negative integer")
    
    config["interval"] = validate_click_interval(config["interval"])
    
    if "target_pos" in config and config["target_pos"] is not None:
        screen = config.get("screen_size", (1920, 1080))
        config["target_pos"] = validate_coordinates(config["target_pos"], screen)
        
    return config
