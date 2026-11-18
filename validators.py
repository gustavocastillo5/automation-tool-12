import logging

logger = logging.getLogger(__name__)

def validate_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """Ensures click coordinates fall within display boundaries."""
    if not (0 <= x < screen_width and 0 <= y < screen_height):
        logger.error(f"Invalid coordinates: ({x}, {y}) for resolution {screen_width}x{screen_height}")
        return False
    return True

def validate_interval(interval: float) -> float:
    """Enforces a minimum safe threshold for clicking frequency."""
    min_interval = 0.01
    if interval < min_interval:
        logger.warning(f"Interval {interval} too low, defaulting to {min_interval}")
        return min_interval
    return float(interval)

def validate_click_count(count: int) -> int:
    """Restricts click count to non-negative integers."""
    if count < 0:
        logger.error(f"Negative click count provided: {count}")
        raise ValueError("Click count cannot be negative")
    return int(count)

def sanitize_config(config: dict) -> dict:
    """Validates entire configuration dictionary structure."""
    required_keys = {'x', 'y', 'interval', 'count'}
    if not required_keys.issubset(config.keys()):
        missing = required_keys - config.keys()
        raise KeyError(f"Missing required configuration keys: {missing}")
    return config