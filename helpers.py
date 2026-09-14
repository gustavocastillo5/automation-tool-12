import math
import random
import time
from typing import Tuple


def cps_to_interval(cps: float) -> float:
    """Convert clicks per second into a delay interval in seconds."""
    if cps <= 0:
        raise ValueError("CPS must be greater than zero.")
    return 1.0 / cps


def add_jitter(delay: float, jitter_percent: float = 0.15) -> float:
    """Add random human-like variation to a click delay."""
    if delay <= 0:
        return 0.0
    variation = delay * jitter_percent
    adjusted = delay + random.uniform(-variation, variation)
    return max(0.001, adjusted)


def calculate_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    """Calculate Euclidean distance between two screen coordinates."""
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])


def clamp_coordinate(x: int, y: int, max_x: int, max_y: int) -> Tuple[int, int]:
    """Ensure screen coordinates stay within screen bounds."""
    clamped_x = max(0, min(x, max_x))
    clamped_y = max(0, min(y, max_y))
    return (clamped_x, clamped_y)


def precise_sleep(duration: float) -> None:
    """High-precision sleep suitable for micro timing in click cycles."""
    end_time = time.perf_counter() + duration
    while time.perf_counter() < end_time:
        time.sleep(0.0001)
