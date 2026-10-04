import random
import time
from typing import Tuple, Optional

def calculate_delay(clicks_per_second: float, humanize: bool = False) -> float:
    """
    Calculate the delay in seconds between clicks.

    If humanize is True, adds a small random deviation to simulate
    human behavior and bypass basic automation detection.
    """
    if clicks_per_second <= 0:
        raise ValueError("Clicks per second must be greater than zero.")

    base_delay = 1.0 / clicks_per_second

    if humanize:
        # Add a random jitter of up to 15% of the base delay
        jitter = random.uniform(-0.15, 0.15) * base_delay
        return max(0.001, base_delay + jitter)

    return base_delay

def parse_coordinate_string(coords: str) -> Optional[Tuple[int, int]]:
    """
    Parse a comma-separated coordinate string (e.g., '100,200') into integer tuple.
    Returns None if the format is invalid.
    """
    try:
        parts = coords.replace(" ", "").split(",")
        if len(parts) != 2:
            return None
        return int(parts[0]), int(parts[1])
    except ValueError:
        return None

def is_within_screen_bounds(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """
    Check if the target coordinates are within the screen boundaries.
    """
    return 0 <= x <= screen_width and 0 <= y <= screen_height

def human_like_pause(min_seconds: float = 0.1, max_seconds: float = 0.5) -> None:
    """
    Pause the execution for a random period to simulate human reaction times.
    """
    duration = random.uniform(min_seconds, max_seconds)
    time.sleep(duration)
