class AutomationError(Exception):
    """Base exception for automation-tool-12."""
    pass

class ClickerNotFoundError(AutomationError):
    """Raised when the target coordinate is unreachable."""
    pass

class RateLimitExceeded(AutomationError):
    """Raised when input events exceed OS safety limits."""
    pass

class ConfigurationError(AutomationError):
    """Raised when the user provides invalid parameters."""
    pass

def validate_coordinates(x: int, y: int):
    """Validates screen boundaries for click events."""
    if x < 0 or y < 0:
        raise ConfigurationError(f"Invalid coordinates: ({x}, {y})")

def handle_automation_exception(e: Exception):
    """Centralized error reporter for the main loop."""
    if isinstance(e, AutomationError):
        print(f"[!] Automation issue detected: {e}")
    else:
        print(f"[!] Critical system failure: {e}")