import time
import logging
from typing import Tuple

logger = logging.getLogger(__name__)


class ClickExecutionError(Exception):
    """Custom exception raised when a click action fails."""
    pass


class ClickProcessor:
    """Handles click execution logic with edge-case validation."""

    def __init__(self, screen_bounds: Tuple[int, int] = (1920, 1080)):
        self.max_x, self.max_y = screen_bounds
        self.is_running = False

    def validate_coordinates(self, x: int, y: int) -> bool:
        """Verify target coordinates are within screen boundaries."""
        if not (0 <= x <= self.max_x and 0 <= y <= self.max_y):
            logger.warning(f"Coordinates ({x}, {y}) out of bounds ({self.max_x}x{self.max_y}).")
            return False
        return True

    def process_click(self, x: int, y: int, interval: float = 0.1) -> bool:
        """Executes a click sequence with safety checks and error handling."""
        if interval <= 0:
            logger.error(f"Invalid click interval: {interval}s. Must be positive.")
            return False

        if not self.validate_coordinates(x, y):
            raise ClickExecutionError(f"Cannot click outside screen bounds: ({x}, {y})")

        try:
            logger.info(f"Positioning cursor at ({x}, {y})")
            time.sleep(interval)
            logger.info(f"Successfully clicked at ({x}, {y})")
            return True
        except PermissionError as pe:
            logger.error(f"Permission denied for input control: {pe}")
            raise ClickExecutionError("Admin privileges required for input automation.") from pe
        except Exception as err:
            logger.error(f"Unexpected error during click action: {err}")
            raise ClickExecutionError(f"Click action failed at ({x}, {y}): {err}") from err
