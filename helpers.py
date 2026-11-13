import time
from typing import Tuple, Optional

def get_coordinates(x: int, y: int) -> Tuple[int, int]:
    """Normalize screen coordinates for click events."""
    screen_width, screen_height = 1920, 1080
    valid_x = max(0, min(x, screen_width))
    valid_y = max(0, min(y, screen_height))
    return valid_x, valid_y

def calculate_delay(interval: float, jitter: float) -> float:
    """Apply minor randomization to click intervals."""
    import random
    return max(0.01, interval + random.uniform(-jitter, jitter))

def format_timestamp(seconds: float) -> str:
    """Convert seconds into human-readable duration string."""
    mins, secs = divmod(int(seconds), 60)
    return f"{mins:02d}m {secs:02d}s"

def validate_bounds(x: int, y: int, boundary: Tuple[int, int, int, int]) -> bool:
    """Check if coordinate falls within restricted window."""
    left, top, right, bottom = boundary
    return left <= x <= right and top <= y <= bottom