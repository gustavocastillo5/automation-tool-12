import random
import time
from typing import Tuple


def calculate_interval(hours: int = 0, minutes: int = 0, seconds: int = 0, milliseconds: int = 0) -> float:
    """Convert hours, minutes, seconds, and milliseconds into total seconds."""
    total_seconds = (hours * 3600) + (minutes * 60) + seconds + (milliseconds / 1000.0)
    return max(0.0, total_seconds)


def apply_random_jitter(base_value: float, jitter_percent: float = 0.1) -> float:
    """Apply a slight random variance to make automated timing appear human-like."""
    if base_value <= 0 or jitter_percent <= 0:
        return max(0.0, base_value)
    delta = base_value * jitter_percent
    jittered_value = base_value + random.uniform(-delta, delta)
    return max(0.001, jittered_value)


def clamp_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> Tuple[int, int]:
    """Ensure x and y coordinates stay within screen bounds."""
    clamped_x = max(0, min(x, screen_width - 1))
    clamped_y = max(0, min(y, screen_height - 1))
    return clamped_x, clamped_y


def human_delay(duration: float, variance: float = 0.1) -> None:
    """Pause execution for a given duration with slight randomized variance."""
    adjusted_duration = apply_random_jitter(duration, variance)
    time.sleep(adjusted_duration)
