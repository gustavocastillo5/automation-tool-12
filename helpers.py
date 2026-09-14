import random
from typing import Tuple


def apply_jitter(coords: Tuple[int, int], radius: int = 3) -> Tuple[int, int]:
    """Apply a small random offset to coordinates to simulate human clicks."""
    x, y = coords
    offset_x = random.randint(-radius, radius)
    offset_y = random.randint(-radius, radius)
    return (max(0, x + offset_x), max(0, y + offset_y))


def calculate_delay(base_cps: float, variance: float = 0.1) -> float:
    """Calculate sleep delay in seconds based on clicks per second and variance."""
    if base_cps <= 0:
        return 0.1
    interval = 1.0 / base_cps
    jitter = random.uniform(-variance, variance) * interval
    return max(0.001, interval + jitter)


def is_within_bounds(coords: Tuple[int, int], screen_size: Tuple[int, int]) -> bool:
    """Check if the given coordinates fall within the specified screen bounds."""
    x, y = coords
    width, height = screen_size
    return 0 <= x < width and 0 <= y < height


def format_duration(seconds: float) -> str:
    """Format total seconds into a readable HH:MM:SS string."""
    mins, secs = divmod(int(seconds), 60)
    hours, mins = divmod(mins, 60)
    return f"{hours:02d}:{mins:02d}:{secs:02d}"
