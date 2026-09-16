import time
import random
from typing import Tuple

def get_random_delay(min_ms: int, max_ms: int) -> float:
    """Calculates a randomized delay in seconds."""
    return random.uniform(min_ms, max_ms) / 1000.0

def validate_coordinates(x: int, y: int, screen_size: Tuple[int, int]) -> bool:
    """Checks if coordinates are within screen boundaries."""
    width, height = screen_size
    return 0 <= x <= width and 0 <= y <= height

def format_runtime(seconds: float) -> str:
    """Converts elapsed seconds into a readable string."""
    hours, remainder = divmod(int(seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def sleep_with_jitter(base_delay: float, jitter_percent: float = 0.1) -> None:
    """Suspends execution for a duration with variance."""
    variation = base_delay * jitter_percent
    actual_delay = base_delay + random.uniform(-variation, variation)
    time.sleep(max(0, actual_delay))