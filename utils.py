import random
import time
from typing import Tuple


def calculate_jitter_delay(base_interval: float, variance: float = 0.1) -> float:
    """Calculate a randomized delay interval to simulate human clicking behavior."""
    if base_interval <= 0:
        return 0.0
    min_delay = max(0.0, base_interval * (1.0 - variance))
    max_delay = base_interval * (1.0 + variance)
    return random.uniform(min_delay, max_delay)


def clamp_coordinates(
    x: int, y: int, screen_bounds: Tuple[int, int, int, int]
) -> Tuple[int, int]:
    """Clamp screen coordinates to remain within the specified screen bounding box.

    screen_bounds format: (min_x, min_y, max_x, max_y)
    """
    min_x, min_y, max_x, max_y = screen_bounds
    clamped_x = max(min_x, min(x, max_x))
    clamped_y = max(min_y, min(y, max_y))
    return clamped_x, clamped_y


def human_sleep(duration_seconds: float) -> None:
    """Sleep for a given duration with small randomized micro-pauses."""
    if duration_seconds <= 0:
        return
    actual_duration = duration_seconds * random.uniform(0.95, 1.05)
    time.sleep(actual_duration)


def parse_click_rate(cps: float) -> float:
    """Convert clicks-per-second (CPS) to an interval duration in seconds."""
    if cps <= 0:
        raise ValueError("Clicks per second must be greater than zero")
    return 1.0 / cps
