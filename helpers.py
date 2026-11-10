import logging
import pyautogui

logger = logging.getLogger(__name__)

def safe_click(x: int, y: int) -> bool:
    """Performs a click with screen boundary and input validation."""
    try:
        screen_width, screen_height = pyautogui.size()
        
        if not (0 <= x < screen_width and 0 <= y < screen_height):
            logger.error(f"Coordinates ({x}, {y}) out of screen bounds")
            return False
            
        pyautogui.click(x, y)
        return True
    except pyautogui.FailSafeException:
        logger.critical("Fail-safe triggered by user intervention")
        return False
    except Exception as e:
        logger.error(f"Unexpected error during click operation: {e}")
        return False

def validate_coordinates(coords: tuple) -> bool:
    """Checks if coordinate tuple is valid numeric format."""
    if not isinstance(coords, tuple) or len(coords) != 2:
        return False
    return all(isinstance(val, int) for val in coords)

def get_screen_safe_dimensions() -> tuple:
    """Retrieves dimensions with fallback to common resolution."""
    try:
        return pyautogui.size()
    except Exception:
        return (1920, 1080)