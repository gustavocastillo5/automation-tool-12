import random
import time
from typing import Tuple


def parse_interval(interval_str: str) -> float:
    """Parse string representation of time interval into seconds."""
    units = {"ms": 0.001, "s": 1.0, "m": 60.0}
    clean_str = interval_str.strip().lower()

    for unit, multiplier in units.items():
        if clean_str.endswith(unit):
            try:
                val = float(clean_str[:-len(unit)].strip())
                return max(0.001, val * multiplier)
            except ValueError:
                break

    try:
        return max(0.001, float(clean_str))
    except ValueError:
        raise ValueError(f"Invalid interval format: {interval_str}")


def apply_jitter(coords: Tuple[int, int], radius: int = 3) -> Tuple[int, int]:
    """Add small random pixel offset to target coordinates for human-like motion."""
    x, y = coords
    offset_x = random.randint(-radius, radius)
    offset_y = random.randint(-radius, radius)
    return (x + offset_x, y + offset_y)


def calculate_random_delay(base_interval: float, variance_pct: float = 0.15) -> float:
    """Calculate interval with randomized variation to simulate natural timing."""
    variance = base_interval * variance_pct
    delay = random.uniform(base_interval - variance, base_interval + variance)
    return max(0.001, delay)


def clamp_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> Tuple[int, int]:
    """Ensure coordinates stay within physical screen boundaries."""
    clamped_x = max(0, min(x, screen_width - 1))
    clamped_y = max(0, min(y, screen_height - 1))
    return (clamped_x, clamped_y)
