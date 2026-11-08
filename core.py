import pyautogui
import time
import logging
from typing import Tuple

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-12')

class AutoClicker:
    """Handles automated mouse interaction cycles."""

    def __init__(self, interval: float = 1.0, clicks: int = 1):
        self.interval = interval
        self.clicks = clicks
        self.is_active = False

    def run_sequence(self, coordinates: Tuple[int, int]) -> None:
        """Executes a click sequence at specified coordinates."""
        self.is_active = True
        logger.info(f"Starting sequence at {coordinates}")
        
        try:
            while self.is_active:
                pyautogui.click(x=coordinates[0], y=coordinates[1], clicks=self.clicks)
                time.sleep(self.interval)
        except KeyboardInterrupt:
            self.stop()
        except Exception as e:
            logger.error(f"Execution error: {e}")
            self.stop()

    def stop(self) -> None:
        """Graceful shutdown of automation sequence."""
        self.is_active = False
        logger.info("Automation sequence halted")

if __name__ == "__main__":
    clicker = AutoClicker(interval=0.5)
    clicker.run_sequence((500, 500))