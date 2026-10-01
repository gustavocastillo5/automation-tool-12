import random
from typing import Tuple, Optional

def calculate_jitter_delay(base_delay: float, jitter: float = 0.1) -> float: 
    """
    Calculate a randomized delay to simulate human-like clicking behavior.

    Args:
        base_delay: The baseline delay between clicks in seconds.
        jitter: The maximum percentage variance to apply (e.g., 0.1 for 10%).

    Returns:
        The calculated delay with applied random jitter, ensuring it is non-negative.
    """
    if base_delay < 0:
        raise ValueError("Base delay cannot be negative.")
    
    variance = base_delay * max(0.0, min(jitter, 1.0))
    actual_delay = base_delay + random.uniform(-variance, variance)
    return max(0.01, actual_delay)

def parse_coordinate_string(coord_str: str) -> Optional[Tuple[int, int]]:
    """
    Parse a string representing screen coordinates into an (X, Y) integer tuple.

    Expected formats include "100,200", "(100, 200)", or "100 , 200".

    Args:
        coord_str: The raw string containing coordinates.

    Returns:
        A tuple of (x, y) integers if parsing succeeds, or None if the format is invalid.
    """
    cleaned = coord_str.strip("() \t\r\n")
    parts = cleaned.split(",")
    if len(parts) != 2:
        return None
    try:
        return int(parts[0].strip()), int(parts[1].strip())
    except ValueError:
        return None

def scale_coordinates(x: int, y: int, scale_factor: float) -> Tuple[int, int]:
    """
    Scale screen coordinates by a specific DPI or scaling factor.

    Args:
        x: The original X-coordinate.
        y: The original Y-coordinate.
        scale_factor: The multiplier for scaling.

    Returns:
        A tuple containing the scaled (X, Y) coordinates as integers.
    """
    scaled_x = int(round(x * scale_factor))
    scaled_y = int(round(y * scale_factor))
    return scaled_x, scaled_y