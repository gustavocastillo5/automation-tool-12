import logging
import pyautogui
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-12')

def execute_click(x: int, y: int, interval: float = 0.1):
    """Performs a screen click with safety validation."""
    try:
        # Ensure coordinates are within reasonable display bounds
        width, height = pyautogui.size()
        if not (0 <= x <= width and 0 <= y <= height):
            raise ValueError(f"Coordinates ({x}, {y}) out of screen bounds")

        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(interval)
        
    except pyautogui.FailSafeException:
        logger.critical("Fail-safe triggered: stopping execution")
        raise
    except pyautogui.PyAutoGUIException as e:
        logger.error(f"PyAutoGUI internal error: {e}")
    except ValueError as e:
        logger.warning(f"Validation error: {e}")
    except Exception as e:
        logger.error(f"Unexpected automation failure: {e}")

def run_sequence(coordinates: list):
    """Iterates through click sequence with error handling."""
    if not coordinates:
        logger.warning("Empty sequence provided, skipping")
        return

    for point in coordinates:
        if not isinstance(point, (tuple, list)) or len(point) != 2:
            logger.error(f"Invalid coordinate format: {point}")
            continue
        execute_click(*point)