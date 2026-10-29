import time
import functools
from typing import Callable, Any

def throttled_execution(interval: float):
    """Decorator to limit function execution frequency for mouse events."""
    def decorator(func: Callable):
        last_called = [0.0]

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            current_time = time.perf_counter()
            elapsed = current_time - last_called[0]
            if elapsed >= interval:
                last_called[0] = current_time
                return func(*args, **kwargs)
            return None
        return wrapper
    return decorator

def batch_process_events(events: list, batch_size: int = 10):
    """Chunking logic to reduce overhead in main loop."""
    for i in range(0, len(events), batch_size):
        yield events[i:i + batch_size]

def fast_timestamp() -> float:
    """High-resolution timing for performance monitoring."""
    return time.perf_counter_ns() / 1_000_000_000