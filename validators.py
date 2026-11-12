from typing import Tuple, Dict, Any


class ValidationError(Exception):
    """Custom exception raised when click parameters violate safety or boundary limits."""
    pass


def validate_screen_coordinates(x: int, y: int, max_bounds: Tuple[int, int] = (3840, 2160)) -> None:
    """Ensure target click coordinates are within acceptable screen boundaries."""
    if not (isinstance(x, int) and isinstance(y, int)):
        raise ValidationError(f"Coordinates must be integers, got ({type(x).__name__}, {type(y).__name__})")
    
    max_x, max_y = max_bounds
    if x < 0 or y < 0:
        raise ValidationError(f"Coordinates cannot be negative: ({x}, {y})")
    if x > max_x or y > max_y:
        raise ValidationError(f"Coordinates ({x}, {y}) exceed display bounds ({max_x}, {max_y})")


def validate_click_interval(interval_ms: float, min_ms: float = 1.0, max_ms: float = 3600000.0) -> float:
    """Validate click interval delay to prevent application freeze or system instability."""
    try:
        interval = float(interval_ms)
    except (ValueError, TypeError) as e:
        raise ValidationError(f"Invalid interval value: '{interval_ms}'") from e

    if interval < min_ms:
        raise ValidationError(f"Interval {interval}ms is too low (minimum allowed: {min_ms}ms)")
    if interval > max_ms:
        raise ValidationError(f"Interval {interval}ms exceeds maximum limit ({max_ms}ms)")

    return interval


def validate_click_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """Comprehensive validation wrapper for autoclicker execution payloads."""
    if not isinstance(config, dict):
        raise ValidationError("Configuration payload must be a valid dictionary")

    required_keys = {"x", "y", "interval_ms", "click_type"}
    missing_keys = required_keys - set(config.keys())
    if missing_keys:
        raise ValidationError(f"Missing required configuration keys: {', '.join(sorted(missing_keys))}")

    valid_buttons = {"left", "right", "middle", "double"}
    if config["click_type"] not in valid_buttons:
        raise ValidationError(f"Unsupported click_type '{config['click_type']}'. Must be one of {valid_buttons}")

    validate_screen_coordinates(config["x"], config["y"])
    config["interval_ms"] = validate_click_interval(config["interval_ms"])
    
    return config
