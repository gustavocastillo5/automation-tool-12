import time
import threading
from queue import Queue

class ClickQueue:
    """Thread-safe buffer for click operations to minimize latency."""
    def __init__(self):
        self._queue = Queue()
        self._stop_event = threading.Event()
        self._worker_thread = threading.Thread(target=self._process, daemon=True)
        self._worker_thread.start()

    def add_click(self, x: int, y: int):
        """Push click task to the processing queue."""
        self._queue.put((x, y))

    def _process(self):
        """Background loop to execute clicks without blocking main logic."""
        import pyautogui
        pyautogui.PAUSE = 0.001
        while not self._stop_event.is_set():
            try:
                coords = self._queue.get(timeout=0.1)
                if coords:
                    pyautogui.click(coords[0], coords[1])
                    self._queue.task_done()
            except Exception:
                continue

    def shutdown(self):
        """Gracefully stop the worker thread."""
        self._stop_event.set()
        self._worker_thread.join()

def batch_process_coordinates(coords: list, handler: callable):
    """Optimization of coordinate iteration using generator expressions."""
    return (handler(x, y) for x, y in coords)