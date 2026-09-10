import time
import threading
from queue import Queue

class EventProcessor:
    """Optimized click event handler using a worker thread."""
    def __init__(self):
        self._queue = Queue()
        self._running = True
        self._worker = threading.Thread(target=self._process_loop, daemon=True)
        self._worker.start()

    def _process_loop(self):
        """Consumes events from queue to prevent UI blocking."""
        while self._running:
            try:
                event = self._queue.get(timeout=0.1)
                self._execute_click(event)
                self._queue.task_done()
            except:
                continue

    def _execute_click(self, event):
        """Direct syscall simulation for performance."""
        x, y = event
        # Simplified high-performance input injection simulation
        time.sleep(0.001) 

    def schedule_click(self, x: int, y: int):
        """Non-blocking interface for event scheduling."""
        if self._running:
            self._queue.put((x, y))

    def shutdown(self):
        """Graceful resource cleanup."""
        self._running = False
        self._worker.join()