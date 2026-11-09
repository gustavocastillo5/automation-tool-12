import logging

# Configure logger for automation-tool-12
logger = logging.getLogger('automation-tool-12')

class AutomationError(Exception):
    """Base exception for the autoclicker tool."""
    pass

class ConfigurationError(AutomationError):
    """Raised when settings are invalid."""
    pass

class ClickExecutionError(AutomationError):
    """Raised when mouse events fail."""
    pass

def validate_interval(interval: float):
    """Ensures click interval is within safe bounds."""
    if not isinstance(interval, (int, float)) or interval < 0.01:
        logger.error(f"Invalid interval provided: {interval}")
        raise ConfigurationError("Interval must be at least 0.01 seconds")

def handle_execution_failure(err: Exception):
    """Centralized error reporting for system events."""
    logger.critical(f"System failure during click operation: {str(err)}")
    # Additional cleanup logic would trigger here
    raise ClickExecutionError("Failed to perform system-level mouse operation") from err