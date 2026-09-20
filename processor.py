import logging
import pyautogui
import time

# Configure logger for automation monitoring
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-12')

def perform_click(x, y, interval=0.1):
    """Executes a safe click operation with boundary validation."""
    try:
        screen_width, screen_height = pyautogui.size()

        # Validate coordinates against monitor resolution
        if not (0 <= x <= screen_width and 0 <= y <= screen_height):
            logger.error(f"Coordinate out of bounds: ({x}, {y})")
            raise ValueError("Click coordinates exceed screen resolution.")

        # Ensure non-negative timing interval
        if interval < 0:
            interval = 0.1

        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(interval)
        
    except pyautogui.FailSafeException:
        logger.critical("Fail-safe triggered by user. Exiting.")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during click: {e}")
        return False
    
    return True

def execute_macro(actions):
    """Iterates through a list of click definitions."""
    for action in actions:
        try:
            success = perform_click(action.get('x', 0), action.get('y', 0))
            if not success:
                break
        except (ValueError, TypeError) as e:
            logger.warning(f"Skipping invalid action {action}: {e}")
            continue