import logging
import pyautogui
import time

# Configure logger for automation monitoring
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-12')

def execute_click(x: int, y: int, delay: float = 0.5):
    """Performs a mouse click with boundary and failure validation."""
    try:
        screen_width, screen_height = pyautogui.size()

        # Validation of screen bounds to prevent out-of-range exceptions
        if not (0 <= x < screen_width and 0 <= y < screen_height):
            logger.error(f"Coordinates ({x}, {y}) out of screen bounds.")
            return False

        # Perform the action
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(delay)
        return True

    except pyautogui.FailSafeException:
        logger.warning("Fail-safe triggered: process aborted by user.")
        return False
    except Exception as e:
        logger.critical(f"Unexpected error during click execution: {e}")
        return False

def safe_execute_sequence(points: list):
    """Handles batch processing with individual point error trapping."""
    for point in points:
        if len(point) != 2:
            logger.warning(f"Skipping invalid point data: {point}")
            continue
        if not execute_click(point[0], point[1]):
            logger.info("Sequence halted due to click failure.")
            break