import time
import logging

try:
    import pyautogui
    pyautogui.FAILSAFE = True
except ImportError:
    class MockPyAutoGUI:
        FAILSAFE = True
        def size(self):
            return (1920, 1080)
        def click(self, x, y):
            pass
    pyautogui = MockPyAutoGUI()

logger = logging.getLogger('automation_tool.core')

class ClickerCore:
    def __init__(self, interval: float = 0.1):
        if interval <= 0:
            raise ValueError('Interval must be a positive float value')
        self.interval = interval
        self.running = False

    def safe_click(self, x: int, y: int) -> bool:
        """Performs a click with boundary safety checks and error handling."""
        try:
            screen_width, screen_height = pyautogui.size()
        except Exception as e:
            logger.error(f'Failed to retrieve screen dimensions: {e}')
            return False

        if not (0 <= x < screen_width and 0 <= y < screen_height):
            logger.warning(f'Click target ({x}, {y}) is out of screen boundaries ({screen_width}x{screen_height})')
            return False

        try:
            pyautogui.click(x, y)
            return True
        except Exception as e:
            logger.error(f'Click execution failed at ({x}, {y}): {e}')
            self.running = False
            return False

    def run_sequence(self, coordinates: list, clicks_count: int = 10):
        """Executes a series of target clicks with safeguard validation."""
        if not coordinates:
            logger.error('No valid coordinates provided for click sequence')
            return

        self.running = True
        clicks_done = 0

        while self.running and clicks_done < clicks_count:
            for x, y in coordinates:
                if not self.running:
                    break
                if not self.safe_click(x, y):
                    logger.warning('Terminating sequence due to click error or fail-safe trigger')
                    self.running = False
                    break
                clicks_done += 1
                time.sleep(self.interval)
        self.running = False