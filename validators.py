def validate_click_parameters(interval, count):
    """
    Validates user input for autoclicker configuration.
    Ensures interval is positive and count is non-negative.
    """
    if not isinstance(interval, (int, float)) or interval <= 0:
        raise ValueError(f"Invalid interval: {interval}. Must be a positive number.")
    
    if not isinstance(count, int) or count < 0:
        raise ValueError(f"Invalid click count: {count}. Must be a non-negative integer.")

    return True

def validate_coordinates(x, y):
    """
    Checks if coordinates fall within typical screen boundaries.
    """
    if not all(isinstance(val, int) for val in [x, y]):
        raise ValueError("Coordinates must be integers.")
    
    if x < 0 or y < 0:
        raise ValueError(f"Negative coordinates detected: ({x}, {y}).")

    return True