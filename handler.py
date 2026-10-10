import pyautogui
import time
from typing import Tuple, Optional

class ClickHandler:
    """Handles mouse click automation logic for the tool."""

    def __init__(self, interval: float = 0.1) -> None:
        """Initialize the clicker with a specified interval."""
        self.interval: float = interval

    def perform_click(self, coordinates: Tuple[int, int]) -> bool:
        """
        Executes a mouse click at the specified (x, y) screen coordinates.
        
        Returns True if successful, False otherwise.
        """
        try:
            x, y = coordinates
            pyautogui.click(x, y)
            time.sleep(self.interval)
            return True
        except (pyautogui.FailSafeException, ValueError) as e:
            print(f"Click execution failed: {e}")
            return False

    def rapid_burst(self, coordinates: Tuple[int, int], count: int) -> None:
        """
        Executes a sequence of clicks at a single location.
        
        :param coordinates: Tuple containing x and y screen positions
        :param count: Number of times to repeat the click
        """
        for _ in range(count):
            self.perform_click(coordinates)

    def get_mouse_position(self) -> Tuple[int, int]:
        """
        Retrieves the current cursor position on the screen.
        """
        pos = pyautogui.position()
        return (int(pos.x), int(pos.y))