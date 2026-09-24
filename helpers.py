import logging

def validate_click_settings(interval, x, y):
    """Validates input parameters for click automation."""
    try:
        if not isinstance(interval, (int, float)) or interval < 0.01:
            raise ValueError("Interval must be a float/int >= 0.01")
        
        if not (isinstance(x, int) and isinstance(y, int)):
            raise ValueError("Coordinates must be integers")
            
        if x < 0 or y < 0:
            raise ValueError("Coordinates cannot be negative")
            
        return True
    except ValueError as e:
        logging.error(f"Validation failed: {e}")
        return False

def sanitize_input(value, default):
    """Ensures input is valid or returns a safe default."""
    try:
        return float(value) if value is not None else default
    except (ValueError, TypeError):
        return default

def validate_bounds(x, y, screen_width, screen_height):
    """Checks if coordinates fall within screen boundaries."""
    return 0 <= x <= screen_width and 0 <= y <= screen_height