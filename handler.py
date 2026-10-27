import logging
import time
from typing import Callable, Tuple, Optional

logger = logging.getLogger("autoclicker.handler")


class ActionExecutionError(Exception):
    """Raised when an automated click action fails unexpectedly."""
    pass


class SafetyTriggeredError(Exception):
    """Raised when safety limits or bounds are violated."""
    pass


class SafeClickHandler:
    """Handles click action dispatch with boundary checks and error recovery."""

    def __init__(self, screen_bounds: Tuple[int, int] = (1920, 1080), max_retries: int = 3):
        self.screen_bounds = screen_bounds
        self.max_retries = max_retries
        self.consecutive_failures = 0

    def validate_coordinates(self, x: int, y: int) -> bool:
        """Ensure target click coordinates fall within display boundaries."""
        max_x, max_y = self.screen_bounds
        if x < 0 or y < 0 or x > max_x or y > max_y:
            logger.warning(f"Coordinates ({x}, {y}) out of bounds (0-{max_x}, 0-{max_y})")
            return False
        return True

    def execute_click(self, click_func: Callable[[int, int], bool], x: int, y: int, delay: float = 0.1) -> bool:
        """Safely execute a click function with edge-case validation and retries."""
        if not self.validate_coordinates(x, y):
            raise SafetyTriggeredError(f"Target position ({x}, {y}) exceeds screen bounds.")

        # Edge case: avoid non-positive or dangerously low delays
        if delay < 0.001:
            logger.warning(f"Interval {delay}s too low; clamping to minimum threshold of 0.001s.")
            delay = 0.001

        for attempt in range(1, self.max_retries + 1):
            try:
                time.sleep(delay)
                if click_func(x, y):
                    self.consecutive_failures = 0
                    return True
                logger.warning(f"Click attempt {attempt} returned non-truthy status.")
            except Exception as exc:
                self.consecutive_failures += 1
                logger.error(f"Unexpected error during click execution (attempt {attempt}): {exc}")

            if self.consecutive_failures >= 5:
                raise ActionExecutionError("Emergency stop triggered due to repeated failure rate.")

        return False
