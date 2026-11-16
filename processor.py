import pyautogui
import time
import logging

# Configure logging for automation events
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-12')

def execute_click(x: int, y: int, interval: float = 0.1):
    """Performs a click with boundary and sanity checks."""
    try:
        # Validate coordinates against screen resolution
        screen_width, screen_height = pyautogui.size()
        
        if not (0 <= x < screen_width and 0 <= y < screen_height):
            logger.error(f"coordinates ({x}, {y}) out of screen bounds")
            return False

        if interval < 0:
            logger.warning("negative interval detected, resetting to default")
            interval = 0.1

        pyautogui.click(x, y)
        time.sleep(interval)
        return True

    except pyautogui.FailSafeException:
        logger.critical("failsafe triggered by user")
        return False
    except Exception as e:
        logger.error(f"unexpected interaction failure: {e}")
        return False

def batch_process(actions: list):
    """Processes list of (x, y) tuples with error propagation."""
    for action in actions:
        if not isinstance(action, (tuple, list)) or len(action) != 2:
            logger.warning(f"skipping malformed action: {action}")
            continue
        
        success = execute_click(action[0], action[1])
        if not success:
            break