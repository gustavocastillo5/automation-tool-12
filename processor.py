import time
import pyautogui
from typing import Tuple, Optional

class ClickProcessor:
    """Handles execution of click operations for automation-tool-12."""

    def __init__(self, interval: float = 0.1) -> None:
        """Initialize processor with specified click interval."""
        self.interval: float = interval

    def perform_click(self, coordinates: Tuple[int, int], button: str = 'left') -> bool:
        """
        Executes a click at the target coordinates.
        
        Args:
            coordinates: Tuple of (x, y) screen positions.
            button: The mouse button to click ('left', 'right', 'middle').
            
        Returns:
            True if click was successful, False otherwise.
        """
        try:
            pyautogui.click(x=coordinates[0], y=coordinates[1], button=button)
            time.sleep(self.interval)
            return True
        except Exception:
            return False

    def batch_process(self, queue: list[Tuple[int, int]], count: int) -> int:
        """
        Processes a queue of coordinates for a specific number of cycles.
        
        Args:
            queue: List of (x, y) coordinate tuples.
            count: Total number of iterations to perform.
            
        Returns:
            The number of successful clicks performed.
        """
        success_count: int = 0
        for _ in range(count):
            for pos in queue:
                if self.perform_click(pos):
                    success_count += 1
        return success_count