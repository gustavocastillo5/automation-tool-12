import random
import time
from typing import Tuple, Optional


def cps_to_interval(cps: float) -> float:
    """Calculate interval in seconds from clicks per second."""
    if cps <= 0:
        raise ValueError("CPS must be greater than zero.")
    return 1.0 / cps


def calculate_jitter_delay(base_interval: float, jitter_percentage: float = 0.1) -> float:
    """Apply random variance to delay interval to simulate human behavior."""
    if base_interval <= 0:
        return 0.0
    variance = base_interval * jitter_percentage
    jittered = random.uniform(base_interval - variance, base_interval + variance)
    return max(0.001, jittered)


def parse_coordinates(coord_str: str) -> Optional[Tuple[int, int]]:
    """Parse coordinate string formatted as 'X,Y' into an integer tuple."""
    try:
        parts = coord_str.strip().split(",")
        if len(parts) != 2:
            return None
        return int(parts[0].strip()), int(parts[1].strip())
    except (ValueError, AttributeError):
        return None


def clamp_coordinates(x: int, y: int, max_x: int, max_y: int) -> Tuple[int, int]:
    """Ensure coordinates fall within valid screen boundaries."""
    clamped_x = max(0, min(x, max_x))
    clamped_y = max(0, min(y, max_y))
    return clamped_x, clamped_y


def human_sleep(duration: float) -> None:
    """Sleep for specified duration with slight micro-variations."""
    if duration <= 0:
        return
    actual_delay = calculate_jitter_delay(duration, jitter_percentage=0.05)
    time.sleep(actual_delay)
