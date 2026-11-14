import pyautogui
import time
import logging

class ClickProcessor:
    """Handles core click execution logic for automation-tool-12."""

    def __init__(self, interval: float = 0.5):
        self.interval = interval
        self.logger = logging.getLogger(__name__)

    def execute_click(self, x: int, y: int, clicks: int = 1) -> None:
        """Performs a mouse click at specified coordinates."""
        try:
            pyautogui.click(x=x, y=y, clicks=clicks)
            self.logger.debug(f"Clicked at ({x}, {y})")
            time.sleep(self.interval)
        except Exception as e:
            self.logger.error(f"Click failure at {x}, {y}: {e}")

    def rapid_click_sequence(self, x: int, y: int, count: int) -> None:
        """Executes a batch of clicks with defined interval."""
        for _ in range(count):
            self.execute_click(x, y)

    @staticmethod
    def get_mouse_position() -> tuple[int, int]:
        """Retrieves current coordinates of the cursor."""
        return pyautogui.position()