class AutoclickerError(Exception):
    """Base exception for all automation-tool-12 errors."""
    pass

class ConfigurationError(AutoclickerError):
    """Raised when the config file is malformed or invalid."""
    pass

class ClickerExecutionError(AutoclickerError):
    """Raised when the clicking operation fails during runtime."""
    pass

class CoordinateOutOfBoundsError(AutoclickerError):
    """Raised when click coordinates fall outside screen bounds."""
    def __init__(self, x, y):
        self.message = f"Coordinates ({x}, {y}) are outside the active screen area."
        super().__init__(self.message)

class InputDeviceError(AutoclickerError):
    """Raised when peripheral control fails or is denied."""
    pass

def validate_coordinates(x, y, width, height):
    """Validates that provided click coordinates are within display limits."""
    if not (0 <= x <= width and 0 <= y <= height):
        raise CoordinateOutOfBoundsError(x, y)
    return True

def handle_exception(e: Exception):
    """Centralized formatter for application-wide exceptions."""
    if isinstance(e, AutoclickerError):
        return f"[CRITICAL] {e.__class__.__name__}: {str(e)}"
    return f"[UNKNOWN] An unexpected error occurred: {str(e)}"