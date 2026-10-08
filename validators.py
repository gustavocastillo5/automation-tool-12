class ValidationError(Exception):
    """Custom exception for input validation failures in automation-tool-12."""
    pass

def validate_click_params(interval, iterations):
    """
    Validates input parameters for the main click loop.
    Ensures interval is positive and iterations are non-negative.
    """
    if not isinstance(interval, (int, float)) or interval <= 0:
        raise ValidationError(f"Invalid interval: {interval}. Must be a positive number.")
    
    if not isinstance(iterations, int) or iterations < 0:
        raise ValidationError(f"Invalid iterations: {iterations}. Must be a non-negative integer.")
    
    return True

def sanitize_coordinates(x, y):
    """
    Validates screen coordinates for the autoclicker.
    Ensures coordinates are within standard display bounds.
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValidationError("Coordinates must be integers.")
    
    if x < 0 or y < 0:
        raise ValidationError(f"Negative coordinates detected: ({x}, {y}).")
    
    return (x, y)