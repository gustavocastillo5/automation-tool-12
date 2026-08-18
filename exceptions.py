class InputValidationError(Exception):
    """Custom exception for input validation errors."""
    pass


def validate_click_interval(interval):
    if not isinstance(interval, (int, float)):
        raise InputValidationError("Click interval must be a number.")
    if interval <= 0:
        raise InputValidationError("Click interval must be greater than zero.")


def validate_click_count(count):
    if not isinstance(count, int):
        raise InputValidationError("Click count must be an integer.")
    if count <= 0:
        raise InputValidationError("Click count must be greater than zero.")


def validate_coordinates(x, y):
    if not (isinstance(x, int) and isinstance(y, int)):
        raise InputValidationError("Coordinates must be integers.")
    if x < 0 or y < 0:
        raise InputValidationError("Coordinates must be non-negative.")
