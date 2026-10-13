def validate_click_settings(interval, duration):
    """
    Validates input ranges for click automation parameters.
    Ensures interval is positive and duration is within bounds.
    """
    MIN_INTERVAL = 0.01
    MAX_DURATION = 3600

    if not isinstance(interval, (int, float)) or interval < MIN_INTERVAL:
        raise ValueError(f"Interval must be at least {MIN_INTERVAL} seconds")
    
    if not isinstance(duration, (int, float)) or duration > MAX_DURATION:
        raise ValueError(f"Duration cannot exceed {MAX_DURATION} seconds")
        
    return True

def validate_coordinates(x, y, screen_width, screen_height):
    """
    Checks if target coordinates are within screen boundaries.
    """
    if not (0 <= x <= screen_width and 0 <= y <= screen_height):
        raise ValueError("Target coordinates are outside screen dimensions")
    return True