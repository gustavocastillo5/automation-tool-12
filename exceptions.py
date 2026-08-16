class ClickError(Exception):
    """Exception raised for errors in the click operation."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidClickDataError(Exception):
    """Exception raised for invalid click data provided."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ClickTimeoutError(Exception):
    """Exception raised when clicking times out."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class PermissionsError(Exception):
    """Exception raised for permission-related issues."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
