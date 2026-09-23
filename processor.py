import time
import threading
from queue import Queue

class EventProcessor:
    """Handles click event execution with background threading."""
    def __init__(self, interval=0.01):
        self.queue = Queue()
        self.interval = interval
        self.running = True

    def submit_event(self, x, y):
        """Adds coordinates to the processing queue."""
        self.queue.put((x, y))

    def run_worker(self):
        """Worker loop for low-latency click execution."""
        while self.running:
            if not self.queue.empty():
                x, y = self.queue.get()
                self._perform_click(x, y)
                time.sleep(self.interval)
            else:
                time.sleep(0.001) # CPU usage reduction

    def _perform_click(self, x, y):
        """Low-level event injection point."""
        # Placeholder for platform-specific mouse interaction
        pass

    def stop(self):
        """Graceful shutdown of worker threads."""
        self.running = False

if __name__ == "__main__":
    processor = EventProcessor()
    worker_thread = threading.Thread(target=processor.run_worker, daemon=True)
    worker_thread.start()