import time
import random
from typing import Tuple

def sleep_randomly(min_sec: float, max_sec: float) -> None:
    """Pauses execution for a randomized duration to simulate human input."""
    duration = random.uniform(min_sec, max_sec)
    time.sleep(duration)

def format_coordinates(x: int, y: int) -> Tuple[int, int]:
    """Validates and ensures coordinates are positive integers."""
    safe_x = max(0, x)
    safe_y = max(0, y)
    return (safe_x, safe_y)

def get_timestamp() -> str:
    """Returns current time string for log entries."""
    return time.strftime('%Y-%m-%d %H:%M:%S')