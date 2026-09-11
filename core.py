import pyautogui
import time
from typing import Tuple

class ClickerCore:
    """Handles the automated clicking operations for the tool."""

    def __init__(self, interval: float = 0.1) -> None:
        """Initialize core with click interval in seconds."""
        self.interval: float = interval

    def perform_click(self, coordinates: Tuple[int, int]) -> None:
        """Executes a mouse click at specific screen coordinates."""
        x, y = coordinates
        pyautogui.click(x=x, y=y)
        time.sleep(self.interval)

    def perform_sequence(self, coordinates_list: list[Tuple[int, int]], count: int) -> None:
        """Iterates through a list of coordinates for a set number of cycles."""
        for _ in range(count):
            for coords in coordinates_list:
                self.perform_click(coords)

    def get_mouse_position(self) -> Tuple[int, int]:
        """Retrieves the current cursor location on the screen."""
        return pyautogui.position()

def validate_coordinates(x: int, y: int) -> bool:
    """Checks if coordinates are within standard screen bounds."""
    screen_width, screen_height = pyautogui.size()
    return 0 <= x <= screen_width and 0 <= y <= screen_height