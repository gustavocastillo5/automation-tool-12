import random
import time
from typing import Tuple, Optional


def calculate_jittered_coords(
    x: int, y: int, jitter_px: int = 3, bounds: Optional[Tuple[int, int, int, int]] = None
) -> Tuple[int, int]:
    """Applies a small random offset to target coordinates to simulate human clicks."""
    offset_x = random.randint(-jitter_px, jitter_px)
    offset_y = random.randint(-jitter_px, jitter_px)
    new_x = x + offset_x
    new_y = y + offset_y

    if bounds:
        min_x, min_y, max_x, max_y = bounds
        new_x = max(min_x, min(new_x, max_x))
        new_y = max(min_y, min(new_y, max_y))

    return new_x, new_y


def get_randomized_delay(base_delay: float, variance_percent: float = 0.15) -> float:
    """Calculates a randomized delay to avoid rigid, detectable click intervals."""
    if base_delay <= 0:
        return 0.0
    variation = base_delay * variance_percent
    return max(0.001, random.uniform(base_delay - variation, base_delay + variation))


def parse_coordinate_string(coord_str: str) -> Tuple[int, int]:
    """Parses a comma-separated string like '100, 200' into x, y tuple."""
    parts = coord_str.split(",")
    if len(parts) != 2:
        raise ValueError("Coordinate string must be formatted as 'x, y'")
    return int(parts[0].strip()), int(parts[1].strip())


def sleep_with_jitter(base_seconds: float, variance_percent: float = 0.15) -> None:
    """Pauses execution for a randomized duration based on base delay."""
    delay = get_randomized_delay(base_seconds, variance_percent)
    time.sleep(delay)
