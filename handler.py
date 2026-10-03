import time
import pyautogui
from typing import Dict, Any, Optional

class ClickHandler:
    """
    Handles automated mouse clicking sequences.
    """

    def __init__(self, settings: Dict[str, Any]) -> None:
        """
        Initialize with click configuration.
        
        :param settings: Dictionary containing interval and duration
        """
        self.interval: float = settings.get("interval", 1.0)
        self.button: str = settings.get("button", "left")

    def perform_click(self, x: int, y: int) -> bool:
        """
        Executes a single mouse click at provided coordinates.

        :param x: Horizontal coordinate
        :param y: Vertical coordinate
        :return: Success status of the action
        """
        try:
            pyautogui.click(x=x, y=y, button=self.button)
            time.sleep(self.interval)
            return True
        except Exception:
            return False

    def run_sequence(self, coordinates: list[tuple[int, int]]) -> None:
        """
        Iterates through a list of coordinates to trigger clicks.

        :param coordinates: List of (x, y) tuples
        """
        for pos in coordinates:
            x, y = pos
            self.perform_click(x, y)

if __name__ == "__main__":
    config: Dict[str, Any] = {"interval": 0.5, "button": "left"}
    handler = ClickHandler(config)
    handler.run_sequence([(100, 100), (200, 200)])