def validate_click_settings(interval, duration):
    """Validates autoclicker timing parameters."""
    if not isinstance(interval, (int, float)) or not isinstance(duration, (int, float)):
        raise ValueError("Interval and duration must be numeric")
    
    if interval < 0.01:
        raise ValueError("Interval must be at least 0.01 seconds")
        
    if duration < 0:
        raise ValueError("Duration cannot be negative")
    
    return True

def validate_coordinates(x, y, screen_width, screen_height):
    """Checks if coordinates fall within display boundaries."""
    if not (0 <= x <= screen_width):
        raise ValueError(f"X coordinate {x} out of bounds")
    if not (0 <= y <= screen_height):
        raise ValueError(f"Y coordinate {y} out of bounds")
    return True

def sanitize_input(user_input, default):
    """Provides basic sanitization for raw user inputs."""
    try:
        return float(user_input)
    except (ValueError, TypeError):
        return default

if __name__ == "__main__":
    # Test validation logic
    try:
        validate_click_settings(0.5, 10)
        validate_coordinates(100, 100, 1920, 1080)
    except ValueError as e:
        print(f"Validation error: {e}")