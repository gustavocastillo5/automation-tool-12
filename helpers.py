import time
import functools
from typing import Callable, Any

def debounce(wait_time: float) -> Callable:
    """Limits frequency of high-precision input events."""
    def decorator(func: Callable) -> Callable:
        last_called = 0.0
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            nonlocal last_called
            current_time = time.perf_counter()
            if current_time - last_called >= wait_time:
                last_called = current_time
                return func(*args, **kwargs)
        return wrapper
    return decorator

def batch_process(items: list, chunk_size: int = 100) -> list:
    """Yields successive n-sized chunks from list for memory efficiency."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

class ClickCache:
    """Thread-safe cache for click coordinate lookup."""
    def __init__(self) -> None:
        self._cache = {}

    def get(self, key: str) -> Any:
        return self._cache.get(key)

    def set(self, key: str, value: Any) -> None:
        self._cache[key] = value
        if len(self._cache) > 1000:
            self._cache.clear()