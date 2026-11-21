import pyautogui
import time
import logging
from threading import Thread, Event

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-12')

class AutoClicker:
    def __init__(self, interval: float = 1.0):
        self.interval = interval
        self.stop_event = Event()
        self._worker_thread = None

    def _click_loop(self):
        """Executes click events until stop signal is received."""
        logger.info("Starting click loop")
        while not self.stop_event.is_set():
            pyautogui.click()
            time.sleep(self.interval)
        logger.info("Click loop terminated")

    def start(self):
        """Initializes and begins execution in a separate thread."""
        if self._worker_thread and self._worker_thread.is_alive():
            return
        self.stop_event.clear()
        self._worker_thread = Thread(target=self._click_loop, daemon=True)
        self._worker_thread.start()

    def stop(self):
        """Signals the loop to exit and cleans up thread."""
        self.stop_event.set()
        if self._worker_thread:
            self._worker_thread.join()

if __name__ == '__main__':
    clicker = AutoClicker(interval=0.5)
    try:
        clicker.start()
        time.sleep(5)
    finally:
        clicker.stop()