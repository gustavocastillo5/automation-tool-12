class AutoclickerError(Exception):
    """Base exception class for all autoclicker-related errors."""
    pass


class InvalidCoordinateError(AutoclickerError):
    """Raised when click coordinates are outside screen dimensions."""

    def __init__(self, x: int, y: int, max_x: int, max_y: int):
        self.x = x
        self.y = y
        self.max_x = max_x
        self.max_y = max_y
        super().__init__(
            f"Coordinates ({x}, {y}) out of screen bounds (0-{max_x}, 0-{max_y})"
        )


class InvalidIntervalError(AutoclickerError):
    """Raised when click interval or delay is mathematically impossible."""

    def __init__(self, interval: float):
        self.interval = interval
        super().__init__(
            f"Click interval must be a positive number, got: {interval}"
        )


class InvalidClickCountError(AutoclickerError):
    """Raised when the requested click count is invalid."""

    def __init__(self, count: int):
        self.count = count
        super().__init__(
            f"Click count must be non-negative or -1 for infinite, got: {count}"
        )


class UnsupportedButtonError(AutoclickerError):
    """Raised when an unrecognized mouse button is specified."""

    def __init__(self, button: str, valid_buttons: list):
        self.button = button
        self.valid_buttons = valid_buttons
        super().__init__(
            f"Unsupported mouse button '{button}'. Choose from: {valid_buttons}"
        )