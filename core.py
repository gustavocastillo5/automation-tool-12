import time
import threading
from typing import Callable, Optional

class HighPrecisionClicker:
    """High-performance auto-clicker execution loop using precise hybrid timing."""

    def __init__(self, click_action: Callable[[], None], interval_ms: float = 10.0):
        self.click_action = click_action
        self.interval = interval_ms / 1000.0
        self._running = False
        self._thread: Optional[threading.Thread] = None

    def start(self) -> None:
        """Start the execution loop in a background thread."""
        if self._running:
            return
        self._running = True
        self._thread = threading.Thread(target=self._click_loop, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        """Stop the execution loop cleanly."""
        self._running = False
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=1.0)

    def _click_loop(self) -> None:
        """Optimized timing loop combining low-overhead sleep with high-precision polling."""
        next_click = time.perf_counter()
        
        while self._running:
            now = time.perf_counter()
            if now >= next_click:
                self.click_action()
                next_click += self.interval
                
                # Prevent backlog compensation when falling behind
                if next_click < now:
                    next_click = now + self.interval

            # Dynamic sleep strategy to maximize timing precision while conserving CPU
            remaining = next_click - time.perf_counter()
            if remaining > 0.002:
                time.sleep(remaining - 0.001)
            elif remaining > 0:
                time.sleep(0)
