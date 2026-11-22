import time
import threading
from typing import Callable

class AutoClicker:
    """Optimized click core utilizing non-blocking thread execution."""
    def __init__(self, interval: float, click_func: Callable[[], None]):
        self.interval = max(0.001, interval)
        self.click_func = click_func
        self._running = False
        self._thread = None

    def _execute(self):
        """High-frequency execution loop with jitter reduction."""
        next_call = time.perf_counter()
        while self._running:
            self.click_func()
            next_call += self.interval
            sleep_time = next_call - time.perf_counter()
            if sleep_time > 0:
                time.sleep(sleep_time)
            else:
                next_call = time.perf_counter()

    def start(self):
        """Initialize execution thread."""
        if not self._running:
            self._running = True
            self._thread = threading.Thread(target=self._execute, daemon=True)
            self._thread.start()

    def stop(self):
        """Graceful shutdown of execution thread."""
        self._running = False
        if self._thread:
            self._thread.join()