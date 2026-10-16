class AutomationError(Exception):
    """Base exception for automation-tool-12."""
    pass

class ClickerConfigurationError(AutomationError):
    """Raised when config parameters are invalid."""
    pass

class CoordinateOutOfBoundsError(AutomationError):
    """Raised when mouse clicks fall outside screen bounds."""
    pass

class DeviceInterfaceError(AutomationError):
    """Raised when input device handles are unreachable."""
    pass

class ExecutionTimeoutError(AutomationError):
    """Raised when an operation exceeds time limits."""
    pass

def validate_bounds(x: int, y: int, screen_width: int, screen_height: int):
    """Checks if coordinate pair is within display resolution."""
    if not (0 <= x <= screen_width and 0 <= y <= screen_height):
        raise CoordinateOutOfBoundsError(f"Coordinates ({x}, {y}) outside resolution {screen_width}x{screen_height}")

def handle_device_failure(error: Exception):
    """Centralized diagnostic for hardware communication issues."""
    # Log the failure and re-raise as custom device error
    raise DeviceInterfaceError(f"System hardware unreachable: {str(error)}")