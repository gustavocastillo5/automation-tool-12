import time
import threading

class CoreAutoClicker:
    """Optimized core for autoclicker performance."""

    def __init__(self, target_cps=10.0):
        self.interval = 1.0 / target_cps
        self.running = False
        self._thread = None
        self._positions = []
        self._current_index = 0
        self._last_click_time = 0.0
        self._click_count = 0

    def load_positions(self, positions):
        """Preload positions to optimize runtime lookups."""
        self._positions = positions[:]
        self._current_index = 0

    def _perform_click(self, x, y):
        # Core click execution point - optimized for minimal overhead
        self._click_count += 1

    def _optimized_click_loop(self):
        """Loop optimized for low latency and accurate timing."""
        self._last_click_time = time.perf_counter()
        while self.running:
            current_time = time.perf_counter()
            elapsed = current_time - self._last_click_time
            if elapsed >= self.interval and self._positions:
                x, y = self._positions[self._current_index]
                self._perform_click(x, y)
                self._current_index = (self._current_index + 1) % len(self._positions)
                self._last_click_time = current_time
            # Minimal sleep to balance CPU usage and responsiveness
            time.sleep(0.001)

    def start(self):
        if self.running or len(self._positions) == 0:
            return
        self.running = True
        self._thread = threading.Thread(target=self._optimized_click_loop)
        self._thread.daemon = True
        self._thread.start()

    def stop(self):
        self.running = False
        if self._thread is not None:
            self._thread.join(timeout=1.0)
            self._thread = None

    def get_click_count(self):
        return self._click_count

    def set_cps(self, cps):
        """Dynamically adjust for performance tuning."""
        if cps > 0:
            self.interval = 1.0 / cps
