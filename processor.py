import time
import threading
from queue import Queue

class EventProcessor:
    """Handles click events using a high-performance worker thread."""

    def __init__(self):
        self.queue = Queue()
        self.running = True
        self.worker = threading.Thread(target=self._process_queue, daemon=True)
        self.worker.start()

    def _process_queue(self):
        """Consumes events from queue with minimal latency."""
        while self.running:
            try:
                task = self.queue.get(timeout=0.1)
                if task:
                    # Unpack event details for rapid execution
                    x, y, btn = task
                    self._execute_click(x, y, btn)
                    self.queue.task_done()
            except:
                continue

    def _execute_click(self, x: int, y: int, btn: str):
        """Low-level interface for click simulation."""
        # Placeholder for platform-specific mouse hooks
        pass

    def add_event(self, x: int, y: int, btn: str):
        """Queues new click event for non-blocking main loop."""
        self.queue.put((x, y, btn))

    def shutdown(self):
        """Graceful stop of background worker."""
        self.running = False
        self.worker.join()