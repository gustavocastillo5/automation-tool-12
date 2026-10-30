class AutomationError(Exception):
    """Base exception for automation-tool-12."""
    pass

class ClickExecutionError(AutomationError):
    """Raised when core click operations fail."""
    pass

class CoordinateOutOfBoundsError(AutomationError):
    """Raised when target coordinates are invalid."""
    pass

class PerformanceBottleneckError(AutomationError):
    """Raised during heavy CPU load detection."""
    pass

def raise_if_bottleneck(cpu_usage: float, threshold: float = 85.0) -> None:
    """Performance monitor for core click loops."""
    if cpu_usage > threshold:
        raise PerformanceBottleneckError(
            f"CPU usage too high ({cpu_usage}%). Throttling execution."
        )

class ValidationError(AutomationError):
    """Raised when input validation fails."""
    pass