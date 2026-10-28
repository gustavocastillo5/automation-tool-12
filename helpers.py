import random
import time
from typing import Tuple


def calculate_jitter_delay(base_interval: float, jitter_percent: float = 0.15) -> float:
    """Calculate a randomized delay interval to simulate human clicking."""
    if base_interval <= 0:
        return 0.0
    
    jitter = base_interval * jitter_percent
    min_delay = max(0.001, base_interval - jitter)
    max_delay = base_interval + jitter
    return random.uniform(min_delay, max_delay)


def is_within_bounds(point: Tuple[int, int], screen_size: Tuple[int, int]) -> bool:
    """Validate if target click coordinates fall within the screen boundaries."""
    x, y = point
    max_x, max_y = screen_size
    return 0 <= x < max_x and 0 <= y < max_y


def cps_to_interval(cps: float) -> float:
    """Convert clicks-per-second (CPS) to time delay interval in seconds."""
    if cps <= 0:
        raise ValueError("CPS value must be strictly positive")
    return 1.0 / cps


def format_elapsed_time(seconds: float) -> str:
    """Format execution duration into HH:MM:SS format."""
    total_seconds = int(seconds)
    hours, remainder = divmod(total_seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"
