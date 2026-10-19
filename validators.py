def validate_click_settings(interval, duration):
    """Ensures click settings are within safe operational bounds."""
    if not isinstance(interval, (int, float)) or interval < 0.01:
        return False, "Interval must be a number greater than 0.01 seconds."
    
    if not isinstance(duration, (int, float)) or duration < 0:
        return False, "Duration must be a positive number."
        
    return True, "Settings valid"

def validate_coordinates(x, y, screen_width, screen_height):
    """Checks if coordinates fall within display bounds."""
    if not (0 <= x <= screen_width and 0 <= y <= screen_height):
        return False, f"Coordinates ({x}, {y}) out of screen bounds."
        
    return True, "Coordinates valid"

def sanitize_input(user_input):
    """Cleans raw input strings to prevent type errors."""
    try:
        return float(user_input)
    except (ValueError, TypeError):
        return None