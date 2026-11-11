import pyautogui
import time
import logging

# Configure basic logger for automation operations
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('automation-tool-12')

class AutoClicker:
    def __init__(self, interval: float = 0.5):
        self.interval = interval
        self.running = False

    def start_clicking(self, iterations: int = 10):
        """Executes mouse clicks based on configured interval."""
        self.running = True
        logger.info(f'starting clicks with {self.interval}s interval')
        
        try:
            for i in range(iterations):
                if not self.running:
                    break
                pyautogui.click()
                time.sleep(self.interval)
                logger.info(f'click {i+1} completed')
        except Exception as e:
            logger.error(f'execution failed: {e}')
        finally:
            self.running = False

    def stop(self):
        """Graceful shutdown of clicker loop."""
        self.running = False
        logger.info('clicker service stopped')

if __name__ == '__main__':
    clicker = AutoClicker(interval=0.1)
    clicker.start_clicking(iterations=5)