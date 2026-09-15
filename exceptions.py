class AutomationError(Exception):
    """Base exception for automation-tool-12."""
    pass

class ClickExecutionError(AutomationError):
    """Raised when click event hardware injection fails."""
    pass

class ConfigValidationError(AutomationError):
    """Raised when configuration parameters are out of bounds."""
    pass

class PerformanceThresholdExceeded(AutomationError):
    """Raised when click interval drops below safe limits."""
    pass

def handle_exception(e: Exception):
    """Centralized handler for runtime automation exceptions."""
    if isinstance(e, ClickExecutionError):
        print(f"Critical hardware failure: {e}")
    elif isinstance(e, PerformanceThresholdExceeded):
        print(f"Throttle intervention required: {e}")
    else:
        print(f"Unexpected system event: {e}")
    return False