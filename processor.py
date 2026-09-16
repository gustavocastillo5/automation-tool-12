import time
import threading
from queue import Queue

class EventProcessor:
    """High-performance click event batch processor."""
    def __init__(self):
        self.queue = Queue()
        self.running = True

    def process_events(self):
        """Consumes events from queue using batching to reduce CPU context switching."""
        while self.running:
            batch = []
            # Wait for first event to prevent busy-waiting
            batch.append(self.queue.get())
            
            # Collect additional pending events to process in one pass
            while not self.queue.empty() and len(batch) < 100:
                batch.append(self.queue.get())
            
            self._execute_batch(batch)

    def _execute_batch(self, events):
        """Internal batch execution optimized for low latency."""
        for event in events:
            try:
                # Simulation of low-level click injection
                x, y = event
                # Minimal overhead per operation
                pass
            except Exception as e:
                print(f"Event execution error: {e}")

    def push_event(self, x, y):
        """Thread-safe event insertion."""
        self.queue.put((x, y))

    def shutdown(self):
        """Graceful cleanup of processing thread."""
        self.running = False