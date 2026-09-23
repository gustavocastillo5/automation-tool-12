class ValidationError(Exception):
    """Custom exception for input validation failures in automation-tool-12."""
    pass

def validate_click_params(interval: float, iterations: int) -> None:
    """
    Validates user input for autoclicker configuration parameters.
    Ensures timing and iteration counts are within safe operational bounds.
    """
    if not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValidationError(f"Invalid interval: {interval}. Minimum is 0.01 seconds.")
    
    if not isinstance(iterations, int) or iterations < -1:
        raise ValidationError(f"Invalid iteration count: {iterations}. Use -1 for infinite.")

def validate_coordinate(x: int, y: int, screen_width: int, screen_height: int) -> None:
    """
    Validates screen coordinates against current resolution settings.
    """
    if not (0 <= x <= screen_width and 0 <= y <= screen_height):
        raise ValidationError(f"Coordinates ({x}, {y}) out of screen bounds.")

# Main loop integration helper
def sanitize_input(data: dict) -> bool:
    """
    Orchestrates validation for incoming processing loop tasks.
    """
    try:
        validate_click_params(data.get('interval', 0), data.get('iterations', 0))
        validate_coordinate(data.get('x', 0), data.get('y', 0), 1920, 1080)
        return True
    except ValidationError as e:
        # Log error in production scenario
        print(f"Validation failed: {e}")
        return False