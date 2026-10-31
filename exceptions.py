"""Custom exception classes for the autoclicker automation tool."""

from typing import Any, Optional


class AutoClickerError(Exception):
    """Base exception class for all autoclicker errors."""

    def __init__(self, message: str, details: Optional[dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message: str = message
        self.details: dict[str, Any] = details or {}

    def __str__(self) -> str:
        if self.details:
            return f"{self.message} | Details: {self.details}"
        return self.message


class TargetNotFoundError(AutoClickerError):
    """Raised when a target screen coordinate or element cannot be found."""

    def __init__(self, target_name: str, region: Optional[tuple[int, int, int, int]] = None) -> None:
        details: dict[str, Any] = {"target_name": target_name}
        if region:
            details["region"] = region
        message = f"Failed to locate target '{target_name}' on screen."
        super().__init__(message, details=details)


class InvalidConfigurationError(AutoClickerError):
    """Raised when autoclicker configuration parameters are invalid."""

    def __init__(self, parameter: str, value: Any, reason: str) -> None:
        details = {"parameter": parameter, "value": value, "reason": reason}
        message = f"Invalid configuration for '{parameter}': {reason} (got {value!r})"
        super().__init__(message, details=details)


class ClickExecutionError(AutoClickerError):
    """Raised when an OS-level mouse click operation fails to execute."""

    def __init__(self, x: int, y: int, button: str = "left", cause: Optional[str] = None) -> None:
        details: dict[str, Any] = {"coordinate": (x, y), "button": button}
        if cause:
            details["cause"] = cause
        message = f"Failed to execute {button} click at position ({x}, {y})."
        super().__init__(message, details=details)


class EmergencyStopError(AutoClickerError):
    """Raised when an emergency stop hotkey is triggered by the user."""

    def __init__(self, trigger_key: str = "esc") -> None:
        details = {"trigger_key": trigger_key}
        message = f"Execution halted by emergency stop hotkey: '{trigger_key}'"
        super().__init__(message, details=details)
