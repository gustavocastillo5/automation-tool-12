def validate_click_settings(interval, duration):
    """Ensures click settings are within safe operational bounds."""
    if not isinstance(interval, (int, float)) or not isinstance(duration, (int, float)):
        raise ValueError("Interval and duration must be numeric.")
    
    if interval < 0.01:
        raise ValueError("Interval must be at least 0.01 seconds.")
    
    if duration < 0:
        raise ValueError("Duration cannot be negative.")
    
    return True

def validate_coordinate_range(x, y, max_x, max_y):
    """Checks if coordinates fall within screen boundaries."""
    if not (0 <= x <= max_x) or not (0 <= y <= max_y):
        raise ValueError(f"Coordinates ({x}, {y}) out of screen bounds.")
    return True

if __name__ == "__main__":
    # Test cases for basic validation logic
    try:
        validate_click_settings(0.1, 5)
        validate_coordinate_range(100, 100, 1920, 1080)
        print("Validation successful")
    except ValueError as e:
        print(f"Validation error: {e}")