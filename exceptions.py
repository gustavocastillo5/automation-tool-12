from typing import Optional

class AutomationError(Exception):
    """Base exception for all automation-tool-12 errors."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.code: Optional[int] = code

class ClickerConnectionError(AutomationError):
    """Raised when the target application connection fails."""
    pass

class InputSequenceError(AutomationError):
    """Raised when an invalid sequence of clicks is provided."""
    pass

class ConfigurationError(AutomationError):
    """Raised when tool settings are invalid or missing."""
    pass

class ExecutionTimeoutError(AutomationError):
    """Raised when an automation task exceeds the time limit."""
    def __init__(self, message: str = "Task timed out") -> None:
        super().__init__(message, code=504)

class ValidationFailedError(AutomationError):
    """Raised when input parameters fail validation checks."""
    pass