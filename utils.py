import time
import logging
import pyautogui
from typing import Tuple

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('automation-tool-12')

def safe_click(x: int, y: int, interval: float = 0.1) -> None:
    """Execute mouse click with safety delay."""
    try:
        pyautogui.click(x, y)
        time.sleep(interval)
    except pyautogui.FailSafeException:
        logger.error("Fail-safe triggered: aborting click.")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during click: {e}")

def get_screen_center() -> Tuple[int, int]:
    """Calculate center coordinates of primary display."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def validate_coordinates(x: int, y: int) -> bool:
    """Verify coordinates fall within screen boundaries."""
    w, h = pyautogui.size()
    return 0 <= x <= w and 0 <= y <= h