import time
import threading
from typing import Callable, Optional


class ClickEngine:
    """High-precision click execution engine with optimized timing loop."""

    def __init__(self, click_action: Callable[[], None]) -> None:
        self._click_action = click_action
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self.interval: float = 0.01

    def start(self, interval: float) -> None:
        """Start the auto-clicking loop with specified interval in seconds."""
        if self._running:
            return
        self.interval = max(0.001, interval)
        self._running = True
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        """Stop the click execution loop."""
        self._running = False
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=1.0)

    def _run_loop(self) -> None:
        """Optimized hybrid timing loop using perf_counter for accuracy."""
        next_time = time.perf_counter()
        
        while self._running:
            self._click_action()
            next_time += self.interval
            
            # Sleep for bulk duration to conserve CPU, micro-spin for precision
            sleep_duration = next_time - time.perf_counter()
            if sleep_duration > 0.002:
                time.sleep(sleep_duration - 0.001)
            
            # Active wait for precise execution timing
            while time.perf_counter() < next_time:
                pass

    @property
    def is_running(self) -> bool:
        return self._running
