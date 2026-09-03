import random
import re
from typing import Tuple

def parse_interval(interval_str: str) -> float:
    """
    Parses a human-readable interval string and returns the value in seconds.

    Supported formats: '100ms', '1.5s', '2m'
    """
    match = re.match(r"^([\d.]+)\s*(ms|s|m)$", interval_str.strip().lower())
    if not match:
        raise ValueError(f"Invalid interval format: {interval_str}")

    value, unit = match.groups()
    num_value = float(value)

    if unit == "ms":
        return num_value / 1000.0
    elif unit == "m":
        return num_value * 60.0
    return num_value

def apply_jitter(base_delay: float, jitter_percent: float) -> float:
    """
    Applies a random variation (jitter) to a base delay.

    The jitter_percent should be between 0.0 and 1.0 representing percentage.
    """
    if not (0.0 <= jitter_percent <= 1.0):
        raise ValueError("Jitter percentage must be between 0.0 and 1.0")

    max_variance = base_delay * jitter_percent
    variance = random.uniform(-max_variance, max_variance)
    return max(0.0, base_delay + variance)

def is_within_screen(coords: Tuple[int, int], resolution: Tuple[int, int]) -> bool:
    """
    Verifies if the target coordinates fall within the specified screen resolution.
    """
    x, y = coords
    width, height = resolution
    return 0 <= x < width and 0 <= y < height
