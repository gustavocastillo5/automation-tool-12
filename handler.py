import time
import pyautogui
from functools import lru_cache

class ClickHandler:
    """Handles high-frequency click execution with performance optimizations."""

    def __init__(self, interval=0.01):
        self.interval = interval
        # Disable fail-safe if performance is critical, otherwise keep default
        pyautogui.FAILSAFE = True

    @lru_cache(maxsize=128)
    def _get_safe_coords(self, x: int, y: int) -> tuple:
        """Cached coordinate normalization to reduce math overhead."""
        return (int(x), int(y))

    def execute_click(self, x: int, y: int):
        """Performs a click using optimized coordinates."""
        coords = self._get_safe_coords(x, y)
        pyautogui.click(x=coords[0], y=coords[1])

    def run_sequence(self, coordinates: list):
        """Optimized batch processing for click sequences."""
        # Local variable caching for tight loops
        click = pyautogui.click
        sleep = time.sleep
        
        for x, y in coordinates:
            click(x=x, y=y)
            if self.interval > 0:
                sleep(self.interval)

# Instance for global access within the tool
click_handler = ClickHandler()