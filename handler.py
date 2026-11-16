import time
import threading
import pyautogui
from queue import Queue

class ClickHandler:
    """Handles high-frequency click events with background threading."""
    def __init__(self, interval: float = 0.01):
        self.interval = interval
        self.click_queue = Queue(maxsize=100)
        self.is_active = False

    def _worker(self):
        """Consumes click coordinates to minimize UI blocking."""
        while self.is_active:
            if not self.click_queue.empty():
                x, y = self.click_queue.get()
                pyautogui.click(x, y)
                time.sleep(self.interval)

    def start_processing(self):
        """Spawns optimized click execution thread."""
        self.is_active = True
        threading.Thread(target=self._worker, daemon=True).start()

    def queue_click(self, x: int, y: int):
        """Adds coordinates to buffer for processing."""
        try:
            self.click_queue.put_nowait((x, y))
        except Exception:
            pass

    def stop(self):
        """Terminates background worker thread."""
        self.is_active = False