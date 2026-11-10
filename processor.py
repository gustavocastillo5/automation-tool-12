import time
import pyautogui
from typing import Tuple, Optional

class ClickProcessor:
    """Handles mouse click automation logic for the tool."""

    def __init__(self, interval: float = 0.1) -> None:
        """Initialize the processor with a click interval."""
        self.interval: float = interval

    def execute_click(self, coordinates: Tuple[int, int], button: str = 'left') -> bool:
        """
        Performs a mouse click at the specified screen coordinates.

        Args:
            coordinates: A tuple of (x, y) screen positions.
            button: The mouse button to click ('left', 'right', 'middle').

        Returns:
            True if the click was successful, False otherwise.
        """
        try:
            x, y = coordinates
            pyautogui.click(x=x, y=y, button=button)
            time.sleep(self.interval)
            return True
        except Exception:
            return False

    def perform_sequence(self, positions: list[Tuple[int, int]]) -> int:
        """
        Iterates through a list of coordinates to perform sequential clicks.

        Args:
            positions: A list of coordinate tuples.

        Returns:
            The count of successfully executed clicks.
        """
        success_count: int = 0
        for pos in positions:
            if self.execute_click(pos):
                success_count += 1
        return success_count