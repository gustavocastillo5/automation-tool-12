class AutomationError(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidClickPositionError(AutomationError):
    """Raised when the click position is invalid."""
    def __init__(self, position):
        super().__init__(f'Invalid click position: {position}')
        self.position = position

class ClickRateExceededError(AutomationError):
    """Raised when click rate exceeds allowed limit."""
    def __init__(self, rate):
        super().__init__(f'Click rate exceeded: {rate}')
        self.rate = rate

class ResourceNotAvailableError(AutomationError):
    """Raised when required resources are not available."""
    def __init__(self, resource):
        super().__init__(f'Resource not available: {resource}')
        self.resource = resource

# Example function demonstrating usage of the exceptions

def click(position, rate):
    if not is_valid_position(position):
        raise InvalidClickPositionError(position)
    if rate > MAX_CLICK_RATE:
        raise ClickRateExceededError(rate)
    if not are_resources_available():
        raise ResourceNotAvailableError('Mouse or Interface')
    # Proceed with click logic
    perform_click(position)

# Helper functions used in the main click logic would be implemented separately.