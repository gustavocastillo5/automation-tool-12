import threading
import time
import ctypes

class PreciseClicker:
    """High-performance autoclicker engine with microsecond timing accuracy."""
    def __init__(self, interval_ms: float = 10.0):
        self.interval = interval_ms / 1000.0
        self.active = False
        self._lock = threading.Lock()
        self._thread = None
        
        # Performance optimization: pre-load Windows DLL if available to minimize latency
        self._is_windows = hasattr(ctypes, "windll")
        if self._is_windows:
            self._mouse_event = ctypes.windll.user32.mouse_event
            # Constants for left click down and up events
            self._click_flags = (0x0002, 0x0004)
            
    def start(self):
        with self._lock:
            if not self.active:
                self.active = True
                self._thread = threading.Thread(target=self._run, daemon=True)
                self._thread.start()

    def stop(self):
        with self._lock:
            self.active = False
        if self._thread:
            self._thread.join()

    def _run(self):
        # Optimization: cache variables in local scope to speed up loop execution
        is_windows = self._is_windows
        click_flags = getattr(self, "_click_flags", None)
        mouse_event = getattr(self, "_mouse_event", None)
        
        target_interval = self.interval
        next_time = time.perf_counter()

        while self.active:
            current_time = time.perf_counter()
            if current_time >= next_time:
                if is_windows and mouse_event:
                    # Directly trigger mouse events bypass high-overhead GUI frameworks
                    mouse_event(click_flags[0], 0, 0, 0, 0)
                    mouse_event(click_flags[1], 0, 0, 0, 0)
                
                next_time = current_time + target_interval

            # Hybrid sleep/spin-lock for extreme timing precision without CPU spiking
            sleep_time = next_time - time.perf_counter()
            if sleep_time > 0.002:
                time.sleep(sleep_time - 0.001)
            else:
                # Spin-lock for high-frequency sub-millisecond precision
                while time.perf_counter() < next_time:
                    pass