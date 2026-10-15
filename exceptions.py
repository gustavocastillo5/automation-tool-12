class AutomationError(Exception):
    """Base exception for automation-tool-12."""
    pass

class ClickerConfigurationError(AutomationError):
    """Raised when clicker parameters are invalid."""
    pass

class CoordinateOutOfBoundsError(AutomationError):
    """Raised when coordinates fall outside screen bounds."""
    pass

class ExecutionInterruptedError(AutomationError):
    """Raised when an automation cycle is manually stopped."""
    pass

class HardwareInteractionError(AutomationError):
    """Raised when input simulation fails."""
    pass

def validate_coordinate(x: int, y: int, screen_width: int, screen_height: int) -> None:
    """Ensure coordinates are within display boundaries."""
    if not (0 <= x < screen_width and 0 <= y < screen_height):
        raise CoordinateOutOfBoundsError(f"Coordinates ({x}, {y}) out of screen bounds.")

def handle_automation_error(e: Exception) -> str:
    """Format exception messages for tool logging."""
    if isinstance(e, AutomationError):
        return f"[AUTOMATION ERROR]: {str(e)}"
    return f"[UNKNOWN ERROR]: {str(e)}"