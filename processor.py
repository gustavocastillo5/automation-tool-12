import logging
import pyautogui
import time

# Configure logger for automation monitoring
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-12')

def perform_click(x, y, interval=0.1):
    """
    Executes a mouse click with input validation and safety checks.
    """
    try:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError('Coordinates must be numeric')

        screen_width, screen_height = pyautogui.size()
        if not (0 <= x <= screen_width and 0 <= y <= screen_height):
            raise pyautogui.FailSafeException('Coordinates out of bounds')

        pyautogui.click(x=x, y=y)
        time.sleep(interval)
        return True

    except pyautogui.FailSafeException as e:
        logger.error(f'Safety trigger activated: {e}')
        return False
    except Exception as e:
        logger.error(f'Unexpected error during click execution: {e}')
        return False

def batch_process_clicks(coordinates):
    """
    Iterates through a list of coordinate tuples with error handling.
    """
    if not isinstance(coordinates, list):
        logger.warning('Invalid input format provided to batch processor')
        return

    for coord in coordinates:
        if len(coord) != 2:
            continue
        success = perform_click(coord[0], coord[1])
        if not success:
            logger.info('Stopping batch processing due to execution failure')
            break