import pyautogui
import time
from typing import Tuple, Optional

class AutoClicker:
    """Automates mouse clicking operations."""

    def __init__(self, interval: float = 0.1) -> None:
        """Initialize the clicker with a specific delay interval."""
        self.interval: float = interval

    def click(self, position: Tuple[int, int]) -> None:
        """Perform a single click at the given coordinates."""
        pyautogui.click(x=position[0], y=position[1])
        time.sleep(self.interval)

    def run(self, coordinates: Tuple[int, int], iterations: int) -> None:
        """Execute a series of clicks at a fixed position."""
        for _ in range(iterations):
            self.click(coordinates)

    def get_mouse_position(self) -> Tuple[int, int]:
        """Retrieve current X and Y mouse coordinates."""
        x, y = pyautogui.position()
        return (int(x), int(y))

    def emergency_stop(self, key: str = 'q') -> Optional[bool]:
        """Check for keypress to halt execution."""
        import keyboard
        if keyboard.is_pressed(key):
            return True
        return False