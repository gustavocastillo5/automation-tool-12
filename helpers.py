import random
import time
from typing import Tuple


def calculate_jittered_delay(base_delay: float, variance: float = 0.1) -> float:
    """Calculate a randomized delay around a base value to simulate human behavior."""
    min_delay = max(0.001, base_delay * (1.0 - variance))
    max_delay = base_delay * (1.0 + variance)
    return random.uniform(min_delay, max_delay)


def apply_coordinate_offset(
    x: int, y: int, max_offset: int = 3
) -> Tuple[int, int]:
    """Apply a small random pixel offset to target coordinates."""
    offset_x = random.randint(-max_offset, max_offset)
    offset_y = random.randint(-max_offset, max_offset)
    return x + offset_x, y + offset_y


def get_region_center(region: Tuple[int, int, int, int]) -> Tuple[int, int]:
    """Calculate center coordinates (x, y) from a region tuple (x, y, width, height)."""
    x, y, width, height = region
    center_x = x + (width // 2)
    center_y = y + (height // 2)
    return center_x, center_y


def convert_interval_to_seconds(value: float, unit: str = "ms") -> float:
    """Convert an interval value and unit into seconds."""
    unit_lower = unit.lower().strip()
    if unit_lower in ("ms", "milliseconds"):
        return max(0.001, value / 1000.0)
    elif unit_lower in ("s", "sec", "seconds"):
        return max(0.001, float(value))
    elif unit_lower in ("m", "min", "minutes"):
        return max(0.001, value * 60.0)
    else:
        raise ValueError(f"Unsupported time unit: {unit}")


def format_cps(click_count: int, elapsed_time: float) -> str:
    """Format current clicks per second (CPS) for display output."""
    if elapsed_time <= 0:
        return "0.0 CPS"
    cps = click_count / elapsed_time
    return f"{cps:.1f} CPS"
