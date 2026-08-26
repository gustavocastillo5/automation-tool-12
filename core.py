import time
import threading
from typing import Callable, Optional

class OptimizedClicker:
    def __init__(self, interval: float = 0.01):
        self.interval = interval
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._lock = threading.Lock()

    def start_clicking(self, action_callback: Callable[[], None]) -> None:
        with self._lock:
            if self._running:
                return
            self._running = True
        
        self._thread = threading.Thread(target=self._click_loop, args=(action_callback,), daemon=True)
        self._thread.start()

    def stop_clicking(self) -> None:
        with self._lock:
            self._running = False
        
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=1.0)

    def _click_loop(self, callback: Callable[[], None]) -> None:
        target_time = time.perf_counter()
        while True:
            with self._lock:
                if not self._running:
                    break
            
            callback()
            
            target_time += self.interval
            sleep_duration = target_time - time.perf_counter()
            
            if sleep_duration > 0:
                time.sleep(sleep_duration)
            else:
                target_time = time.perf_counter()