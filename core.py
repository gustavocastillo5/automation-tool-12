import pyautogui
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-12')

def execute_click(x: int, y: int, interval: float = 0.1) -> bool:
    """Performs a click operation with safety bounds and error handling."""
    try:
        # Validate coordinates against screen boundaries
        screen_width, screen_height = pyautogui.size()
        if not (0 <= x < screen_width and 0 <= y < screen_height):
            logger.error(f"coordinates ({x}, {y}) out of screen bounds")
            return False
            
        # Fail-safe: moving mouse to corner aborts execution
        pyautogui.FAILSAFE = True
        
        pyautogui.click(x, y)
        time.sleep(interval)
        return True
        
    except pyautogui.FailSafeException:
        logger.warning("failsafe triggered, aborting automation")
        return False
    except Exception as e:
        logger.error(f"unexpected failure during click: {e}")
        return False

def run_sequence(clicks: list) -> None:
    """Iterates through click tasks with basic state verification."""
    for i, coords in enumerate(clicks):
        success = execute_click(*coords)
        if not success:
            logger.info(f"sequence halted at index {i}")
            break