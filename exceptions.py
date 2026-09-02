"""Custom exceptions for automation-tool-12 autoclicker.
This module centralizes all error types for the tool.
"""

from typing import Optional, Dict, Any

class AutoclickerError(Exception):
    """Base class for autoclicker specific exceptions."""
    def __init__(self, message: str, context: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message = message
        self.context = context or {}
    def __str__(self) -> str:
        if self.context:
            ctx = ", ".join([f"{k}={v}" for k, v in self.context.items()])
            return f"{self.message} | Context: {ctx}"
        return self.message

class ClickError(AutoclickerError):
    """Exception for failed click operations."""
    def __init__(self, x: int, y: int, reason: str = "unknown") -> None:
        msg = f"Click failed at ({x}, {y}): {reason}"
        super().__init__(msg, {"x": x, "y": y, "reason": reason})

class InvalidCoordinatesError(AutoclickerError):
    """Raised when provided coordinates are invalid."""
    def __init__(self, x: int, y: int) -> None:
        super().__init__(f"Invalid coordinates: ({x}, {y})", {"x": x, "y": y})

class HotkeyError(AutoclickerError):
    """Error related to hotkey registration or triggering."""
    def __init__(self, hotkey: str) -> None:
        super().__init__(f"Hotkey error: {hotkey}", {"hotkey": hotkey})

class ScreenCaptureError(AutoclickerError):
    """Raised on failure to capture screen content."""
    pass

class TemplateMatchError(AutoclickerError):
    """When no match found for image template."""
    def __init__(self, template: str, confidence: float = 0.8) -> None:
        msg = f"No match for template '{template}' at confidence {confidence}"
        super().__init__(msg, {"template": template, "confidence": confidence})

class OperationTimeoutError(AutoclickerError):
    """Raised when autoclicker operation times out."""
    def __init__(self, op_name: str, seconds: float) -> None:
        super().__init__(f"Timeout during {op_name} after {seconds}s", {"operation": op_name, "timeout": seconds})

class ConfigError(AutoclickerError):
    """Configuration related errors."""
    def __init__(self, setting: str, issue: str) -> None:
        super().__init__(f"Config error - {setting}: {issue}", {"setting": setting, "issue": issue})

class PermissionDeniedError(AutoclickerError):
    """OS level permission issues for automation."""
    pass

# Helper to format exceptions
def format_exception(exc: Exception) -> str:
    """Return formatted string for any exception."""
    if isinstance(exc, AutoclickerError):
        return str(exc)
    return f"Unexpected: {str(exc)}"