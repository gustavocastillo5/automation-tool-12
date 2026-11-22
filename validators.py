import logging

def validate_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """Ensures click coordinates are within display bounds."""
    try:
        if not (0 <= x <= screen_width and 0 <= y <= screen_height):
            logging.warning(f"Coordinates ({x}, {y}) outside screen boundaries.")
            return False
        return True
    except TypeError:
        logging.error("Invalid input types provided for coordinate validation.")
        return False

def validate_interval(interval: float) -> float:
    """Sanitizes click interval to prevent system resource exhaustion."""
    MIN_INTERVAL = 0.01
    try:
        val = float(interval)
        if val < MIN_INTERVAL:
            logging.info(f"Interval {val} below threshold, resetting to {MIN_INTERVAL}.")
            return MIN_INTERVAL
        return val
    except (ValueError, TypeError):
        logging.error("Invalid interval format; defaulting to 1.0 second.")
        return 1.0

def validate_click_count(count: int) -> int:
    """Ensures click count is a positive integer or zero for infinite."""
    try:
        val = int(count)
        if val < 0:
            return 0
        return val
    except (ValueError, TypeError):
        logging.error("Invalid click count provided; defaulting to 1.")
        return 1