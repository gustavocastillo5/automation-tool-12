import random
import re
from typing import Tuple


def parse_time_interval(interval_str: str) -> float:
    """Parses a time interval string (e.g., '500ms', '1.5s', '2m') into seconds."""
    match = re.match(r"^([\d.]+)\s*(ms|s|m)$", interval_str.strip().lower())
    if not match:
        raise ValueError(
            f"Invalid interval format: {interval_str}. Use e.g., '100ms', '1.5s', '2m'"
        )

    value, unit = match.groups()
    val_float = float(value)

    if unit == "ms":
        return val_float / 1000.0
    elif unit == "m":
        return val_float * 60.0
    return val_float


def apply_jitter(value: float, percentage: float = 0.1) -> float:
    """Applies a small random variation to an interval to mimic human behavior."""
    if percentage <= 0:
        return value
    variance = value * percentage
    return max(0.0, value + random.uniform(-variance, variance))


def clamp_coordinates(
    coords: Tuple[int, int], max_width: int, max_height: int
) -> Tuple[int, int]:
    """Clamps click coordinates to ensure they are within safe screen boundaries."""
    x, y = coords
    clamped_x = max(0, min(x, max_width - 1))
    clamped_y = max(0, min(y, max_height - 1))
    return clamped_x, clamped_y


def format_cps(interval: float) -> float:
    """Calculates clicks per second (CPS) based on sleep interval."""
    if interval <= 0:
        return 0.0
    return round(1.0 / interval, 2)
