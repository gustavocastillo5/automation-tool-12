import logging
import pyautogui
from exceptions import ClickerError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def safe_click(x: int, y: int):
    """Executes a click with boundary and system checks."""
    try:
        screen_width, screen_height = pyautogui.size()
        
        if not (0 <= x <= screen_width and 0 <= y <= screen_height):
            raise ClickerError(f"Coordinates ({x}, {y}) out of screen bounds")
            
        pyautogui.click(x, y)
        logger.info(f"Successfully clicked at {x}, {y}")
        
    except pyautogui.FailSafeException:
        logger.error("Fail-safe triggered by user movement")
        raise
    except Exception as e:
        logger.error(f"Unexpected automation failure: {e}")
        raise ClickerError("Automation operation failed") from e

def validate_coordinates(coords: tuple):
    """Validates input structure for automation sequence."""
    if not isinstance(coords, tuple) or len(coords) != 2:
        raise ValueError("Coordinates must be a tuple of (x, y)")
    
    if not all(isinstance(val, int) for val in coords):
        raise TypeError("Coordinate values must be integers")
    
    return True