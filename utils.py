import random
import time
from typing import Tuple, Union


def calculate_jittered_delay(base_delay: float, jitter_percent: float = 0.1) -> float:
    """Calculate a randomized delay to simulate human-like clicking behavior.

    Args:
        base_delay: Target delay in seconds between clicks.
        jitter_percent: Maximum percentage variation allowed (0.0 to 1.0).

    Returns:
        A randomized float delay in seconds, guaranteed to be non-negative.
    """
    if base_delay <= 0:
        return 0.0

    variation = base_delay * min(max(jitter_percent, 0.0), 1.0)
    delay = random.uniform(base_delay - variation, base_delay + variation)
    return max(0.001, delay)


def offset_coordinates(
    coords: Tuple[int, int], radius: int
) -> Tuple[int, int]:
    """Apply a random spatial offset within a radius to target coordinates.

    Args:
        coords: Original (x, y) pixel coordinates.
        radius: Maximum pixel distance to offset in any direction.

    Returns:
        A tuple of (x, y) integer coordinates with random offset applied.
    """
    if radius <= 0:
        return coords

    x_offset = random.randint(-radius, radius)
    y_offset = random.randint(-radius, radius)
    return coords[0] + x_offset, coords[1] + y_offset


def cps_to_interval(cps: Union[int, float]) -> float:
    """Convert clicks per second (CPS) into a time interval between clicks.

    Args:
        cps: Target clicks per second rate.

    Returns:
        Delay interval in seconds per click.

    Raises:
        ValueError: If cps is less than or equal to zero.
    """
    if cps <= 0:
        raise ValueError("CPS rate must be greater than zero.")
    return 1.0 / float(cps)


def precise_sleep(duration: float) -> None:
    """Sleep with high precision for short timing loops.

    Args:
        duration: Time to sleep in seconds.
    """
    if duration <= 0:
        return

    end_time = time.perf_counter() + duration
    while time.perf_counter() < end_time:
        remaining = end_time - time.perf_counter()
        if remaining > 0.002:
            time.sleep(remaining - 0.001)
