def validate_click_settings(interval, duration):
    """Ensures click settings are within safe operational bounds."""
    if not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValueError("Interval must be a float or int >= 0.01 seconds.")
    if not isinstance(duration, (int, float)) or duration < 0:
        raise ValueError("Duration must be a positive number.")
    return True

def validate_coordinates(x, y):
    """Checks if coordinates are non-negative screen integers."""
    if not (isinstance(x, int) and isinstance(y, int)):
        raise TypeError("Coordinates must be integers.")
    if x < 0 or y < 0:
        raise ValueError("Coordinates cannot be negative.")
    return True

def sanitize_input(user_input, default):
    """Returns user input if valid, otherwise returns default."""
    try:
        return float(user_input) if user_input else default
    except ValueError:
        return default