import time
import threading
from functools import lru_cache

@lru_cache(maxsize=128)
def get_normalized_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> tuple:
    """Calculates coordinate percentages to support various display resolutions."""
    return (x / screen_width, y / screen_height)

class ClickOptimizer:
    """Buffer-based event handling to reduce CPU overhead during rapid clicks."""
    def __init__(self, interval: float = 0.01):
        self.interval = interval
        self._last_call = 0.0
        self._lock = threading.Lock()

    def is_throttled(self) -> bool:
        """Prevents system event flooding by enforcing minimum click delay."""
        with self._lock:
            current_time = time.perf_counter()
            if current_time - self._last_call < self.interval:
                return True
            self._last_call = current_time
            return False

def batch_process_coordinates(coords: list, scale_x: int, scale_y: int) -> list:
    """Vectorized coordinate scaling for performance optimization."""
    return [
        (int(x * scale_x), int(y * scale_y)) 
        for x, y in coords
    ]