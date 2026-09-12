import random
import time
from typing import Tuple


def calculate_jitter_delay(base_delay: float, jitter: float) -> float:
    """Calculate a randomized delay duration to simulate human clicking.

    Args:
        base_delay: The target delay between clicks in seconds.
        jitter: The maximum percentage variance allowed (0.0 to 1.0).

    Returns:
        A randomized delay time in seconds.
    """
    if jitter <= 0:
        return max(0.0, base_delay)

    variance = base_delay * min(jitter, 1.0)
    low = max(0.0, base_delay - variance)
    high = base_delay + variance
    return random.uniform(low, high)


def parse_coordinate_string(coord_str: str) -> Tuple[int, int]:
    """Parse a formatted string 'X,Y' into an integer coordinate tuple.

    Args:
        coord_str: A string representing coordinates in 'X,Y' format.

    Returns:
        A tuple containing (x, y) integer coordinates.

    Raises:
        ValueError: If the string format is invalid or non-numeric.
    """
    parts = coord_str.strip().split(",")
    if len(parts) != 2:
        raise ValueError("Coordinates must be in 'X,Y' format")

    x_val, y_val = parts[0].strip(), parts[1].strip()
    return int(x_val), int(y_val)


def sleep_with_precision(duration: float) -> None:
    """Pause execution for a specific duration using high-precision sleep.

    Args:
        duration: Total sleep duration in seconds.
    """
    if duration <= 0:
        return

    end_time = time.perf_counter() + duration
    while time.perf_counter() < end_time:
        remaining = end_time - time.perf_counter()
        if remaining > 0.002:
            time.sleep(remaining - 0.001)
