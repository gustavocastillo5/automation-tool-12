import time
import pyautogui
from typing import Dict, Any

class ClickProcessor:
    """Handles execution of click sequences based on provided configuration."""

    def __init__(self, config: Dict[str, Any]):
        self.interval = config.get('interval', 0.1)
        self.clicks = config.get('clicks', 1)
        self.button = config.get('button', 'left')

    def execute_sequence(self, coordinates: list) -> None:
        """Iterates through coordinate list and performs automated clicks."""
        for x, y in coordinates:
            try:
                pyautogui.click(x=x, y=y, clicks=self.clicks, button=self.button)
                time.sleep(self.interval)
            except pyautogui.FailSafeException:
                print("Fail-safe triggered: stopping processor.")
                break
            except Exception as e:
                print(f"Click error at ({x}, {y}): {e}")

    def set_config(self, new_config: Dict[str, Any]) -> None:
        """Updates click execution parameters."""
        self.interval = new_config.get('interval', self.interval)
        self.clicks = new_config.get('clicks', self.clicks)
        self.button = new_config.get('button', self.button)