import random
import time
from typing import Tuple


def calculate_delay(cps: float, jitter: float = 0.1) -> float:
    """Calculate sleep delay based on clicks per second and random jitter."""
    if cps <= 0:
        raise ValueError("CPS must be greater than zero.")
    base_delay = 1.0 / cps
    # Apply percentage jitter randomly (-jitter to +jitter)
    variation = base_delay * random.uniform(-jitter, jitter)
    return max(0.001, base_delay + variation)


def sleep_with_jitter(cps: float, jitter: float = 0.1) -> None:
    """Pause execution for a duration calculated from CPS and jitter."""
    delay = calculate_delay(cps, jitter)
    time.sleep(delay)


def get_randomized_coordinates(x: int, y: int, radius: int = 3) -> Tuple[int, int]:
    """Apply slight random pixel offset to target coordinates to mimic human input."""
    if radius <= 0:
        return x, y
    offset_x = random.randint(-radius, radius)
    offset_y = random.randint(-radius, radius)
    return x + offset_x, y + offset_y


def parse_coordinate_string(coords_str: str) -> Tuple[int, int]:
    """Parse 'X,Y' string input into integer tuple coordinates."""
    parts = coords_str.strip().split(",")
    if len(parts) != 2:
        raise ValueError("Coordinates must be in 'X,Y' format.")
    return int(parts[0].strip()), int(parts[1].strip())
