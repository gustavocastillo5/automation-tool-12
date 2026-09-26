import time
import logging

logger = logging.getLogger("autoclicker.processor")

class ClickProcessor:
    """Processes and validates click actions with error handling for edge cases."""

    def __init__(self, screen_width: int = 1920, screen_height: int = 1080):
        if screen_width <= 0 or screen_height <= 0:
            raise ValueError("Screen dimensions must be positive integers")
        self.screen_width = screen_width
        self.screen_height = screen_height

    def validate_coordinates(self, x: int, y: int) -> tuple[int, int]:
        """Validates and clamps coordinates to the screen boundaries."""
        try:
            # Clamp coordinates to ensure they fall within valid screen space
            clamped_x = max(0, min(int(x), self.screen_width - 1))
            clamped_y = max(0, min(int(y), self.screen_height - 1))
            return clamped_x, clamped_y
        except (TypeError, ValueError):
            logger.error(f"Invalid coordinate type or value: {x}, {y}. Defaulting to (0,0)")
            return 0, 0

    def execute_click(self, x: int, y: int, interval: float) -> bool:
        """Safely executes a single click action after a specified interval."""
        safe_x, safe_y = self.validate_coordinates(x, y)
        
        # Prevent negative or extremely tiny sleep intervals leading to CPU thrashing
        try:
            safe_interval = max(0.001, float(interval))
        except (TypeError, ValueError):
            logger.warning("Invalid interval provided. Defaulting to 0.1s")
            safe_interval = 0.1

        try:
            time.sleep(safe_interval)
            # Simulated OS click action for environment safety
            # In a GUI system, this would trigger actual mouse actions
            logger.debug(f"Simulated click executed at ({safe_x}, {safe_y}) after {safe_interval}s")
            return True
        except Exception as exc:
            logger.error(f"Failed to execute click at ({safe_x}, {safe_y}): {exc}")
            return False

    def process_batch(self, points: list[tuple[int, int]], interval: float) -> int:
        """Processes a batch of click coordinates, counting successful operations."""
        successful_clicks = 0
        if not points:
            logger.warning("Empty batch of coordinates passed to processor")
            return 0

        for x, y in points:
            if self.execute_click(x, y, interval):
                successful_clicks += 1
        return successful_clicks