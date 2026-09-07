import random
import time
from typing import Tuple


def calculate_jittered_point(
    point: Tuple[int, int], max_jitter: int = 3
) -> Tuple[int, int]:
    """Applies random pixel offsets to simulate human mouse precision."""
    x, y = point
    offset_x = random.randint(-max_jitter, max_jitter)
    offset_y = random.randint(-max_jitter, max_jitter)
    return (max(0, x + offset_x), max(0, y + offset_y))


def generate_human_delay(
    base_delay: float, variance_ratio: float = 0.15
) -> float:
    """Calculates a randomized delay duration based on base value and variance."""
    if base_delay <= 0:
        return 0.0
    min_delay = base_delay * (1.0 - variance_ratio)
    max_delay = base_delay * (1.0 + variance_ratio)
    return max(0.001, random.uniform(min_delay, max_delay))


def is_valid_screen_position(
    point: Tuple[int, int], screen_bounds: Tuple[int, int]
) -> bool:
    """Checks if a target click point falls within valid screen boundaries."""
    x, y = point
    max_x, max_y = screen_bounds
    return 0 <= x <= max_x and 0 <= y <= max_y


def sleep_with_interruption(
    duration: float, check_interval: float = 0.05
) -> bool:
    """Sleeps for duration while allowing periodic execution pause checks."""
    end_time = time.time() + duration
    while time.time() < end_time:
        remaining = end_time - time.time()
        time.sleep(min(remaining, check_interval))
    return True
