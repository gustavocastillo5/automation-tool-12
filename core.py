import pyautogui
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-12')

def perform_click(x: int, y: int, interval: float = 0.1):
    """Executes a safe click operation with boundary checks."""
    try:
        screen_width, screen_height = pyautogui.size()
        
        if not (0 <= x <= screen_width and 0 <= y <= screen_height):
            logger.error(f"coordinates ({x}, {y}) out of screen bounds")
            return False
            
        if interval < 0:
            logger.warning("negative interval provided, resetting to default")
            interval = 0.1

        pyautogui.click(x, y)
        time.sleep(interval)
        return True
        
    except pyautogui.FailSafeException:
        logger.critical("failsafe triggered, aborting operation")
        return False
    except Exception as e:
        logger.error(f"unexpected execution error: {e}")
        return False

def run_automation(coords: list, duration: float):
    """Iterates through click tasks with error handling."""
    for x, y in coords:
        success = perform_click(x, y, duration)
        if not success:
            logger.info("skipping coordinate due to error")
            continue