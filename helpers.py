import logging
import pyautogui
from typing import Tuple, Optional

logger = logging.getLogger(__name__)

def get_safe_coordinates(x: int, y: int) -> Optional[Tuple[int, int]]:
    """Validates coordinates against current screen resolution."""
    try:
        screen_width, screen_height = pyautogui.size()
        if 0 <= x < screen_width and 0 <= y < screen_height:
            return (x, y)
        logger.warning(f"Coordinates ({x}, {y}) out of screen bounds.")
        return None
    except pyautogui.FailSafeException:
        logger.critical("Fail-safe triggered: mouse moved to corner.")
        return None
    except Exception as e:
        logger.error(f"Unexpected error validating coordinates: {e}")
        return None

def perform_safe_click(x: int, y: int, button: str = 'left') -> bool:
    """Executes a click with boundary and permission validation."""
    coords = get_safe_coordinates(x, y)
    if not coords:
        return False

    try:
        pyautogui.click(x=coords[0], y=coords[1], button=button)
        return True
    except pyautogui.ImageNotFoundException:
        logger.error("Target element not found on screen.")
    except Exception as e:
        logger.error(f"Click execution failed: {e}")
    return False