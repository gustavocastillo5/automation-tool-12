import random
import re
from typing import Tuple


def calculate_jitter(delay: float, jitter_percent: float = 10.0) -> float:
    """Add small random variation to click delay to simulate human behavior."""
    if delay <= 0:
        return 0.0
    variation = delay * (jitter_percent / 100.0)
    jittered = random.uniform(delay - variation, delay + variation)
    return max(0.001, round(jittered, 4))


def clamp_coordinates(x: int, y: int, max_x: int, max_y: int) -> Tuple[int, int]:
    """Ensure target click coordinates stay within current screen bounds."""
    clamped_x = max(0, min(x, max_x))
    clamped_y = max(0, min(y, max_y))
    return clamped_x, clamped_y


def parse_interval(interval_str: str) -> float:
    """Convert time strings like '50ms', '1.5s', or '2m' to seconds."""
    match = re.match(r"^(\d+(?:\.\d+)?)\s*(ms|s|m|h)?$", interval_str.strip().lower())
    if not match:
        raise ValueError(f"Invalid interval duration format: '{interval_str}'")

    val_str, unit = match.groups()
    value = float(val_str)

    multipliers = {
        "ms": 0.001,
        "s": 1.0,
        "m": 60.0,
        "h": 3600.0,
    }
    return round(value * multipliers.get(unit, 1.0), 4)


def format_elapsed_time(seconds: float) -> str:
    """Format active execution time into a standard HH:MM:SS string."""
    total_sec = int(seconds)
    hours = total_sec // 3600
    minutes = (total_sec % 3600) // 60
    secs = total_sec % 60

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"
