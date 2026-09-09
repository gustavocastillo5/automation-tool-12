import logging

def validate_interval(interval: float) -> float:
    """Ensures click interval is within safe operational bounds."""
    min_interval = 0.01
    max_interval = 60.0
    if not (min_interval <= interval <= max_interval):
        logging.warning(f"Interval {interval}s out of range. Defaulting to 1.0s.")
        return 1.0
    return interval

def validate_coordinates(x: int, y: int) -> tuple[int, int]:
    """Checks if provided coordinates are non-negative integers."""
    safe_x = max(0, x)
    safe_y = max(0, y)
    return (safe_x, safe_y)

def validate_clicks(count: int) -> int:
    """Limits click count to prevent system freezing."""
    if count < 0:
        return 0
    if count > 10000:
        return 10000
    return count

def sanitize_input(data: dict) -> dict:
    """Applies validation rules to the user configuration dictionary."""
    return {
        "interval": validate_interval(data.get("interval", 1.0)),
        "coords": validate_coordinates(data.get("x", 0), data.get("y", 0)),
        "count": validate_clicks(data.get("count", 1))
    }