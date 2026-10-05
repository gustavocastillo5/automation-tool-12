from typing import Optional

class AutomationError(Exception):
    """Base exception class for automation-tool-12."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.code = code

class ClickerConfigurationError(AutomationError):
    """Raised when the autoclicker configuration is invalid."""
    pass

class ExecutionTimeoutError(AutomationError):
    """Raised when an automation task exceeds its time limit."""
    pass

class InputDeviceNotFoundError(AutomationError):
    """Raised when the mouse or keyboard hardware is missing."""
    pass

class ClickerInterruptError(AutomationError):
    """Raised when the user manually cancels an active task."""
    def __init__(self, message: str = "Task execution interrupted by user") -> None:
        super().__init__(message, code=403)