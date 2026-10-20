class AutomationError(Exception):
    """Base exception class for automation-tool-12."""
    pass


class ClickerConfigurationError(AutomationError):
    """Raised when the configuration file is invalid or missing."""
    def __init__(self, message: str, config_path: str) -> None:
        self.config_path: str = config_path
        super().__init__(f"{message} (path: {config_path})")


class InputDeviceError(AutomationError):
    """Raised when mouse or keyboard control fails."""
    def __init__(self, device: str, details: str) -> None:
        self.device: str = device
        super().__init__(f"failed to interact with {device}: {details}")


class ExecutionTimeoutError(AutomationError):
    """Raised when an automation task exceeds its runtime limit."""
    def __init__(self, task_name: str, duration: float) -> None:
        self.task_name: str = task_name
        super().__init__(f"task {task_name} timed out after {duration} seconds")


class PermissionDeniedError(AutomationError):
    """Raised when the tool lacks necessary OS privileges."""
    def __init__(self, requirement: str) -> None:
        self.requirement: str = requirement
        super().__init__(f"insufficient permissions for: {requirement}")