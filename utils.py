import time
import random
from typing import Tuple

def get_random_delay(min_ms: int, max_ms: int) -> float:
    """
    Calculate a random delay in seconds between two millisecond bounds.

    :param min_ms: Minimum delay in milliseconds
    :param max_ms: Maximum delay in milliseconds
    :return: Delay duration in seconds
    """
    delay_ms = random.uniform(min_ms, max_ms)
    return delay_ms / 1000.0

def validate_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """
    Check if the provided coordinates fall within screen boundaries.

    :param x: X coordinate to check
    :param y: Y coordinate to check
    :param screen_width: Maximum horizontal bounds
    :param screen_height: Maximum vertical bounds
    :return: True if coordinates are valid
    """
    return 0 <= x < screen_width and 0 <= y < screen_height

def format_execution_time(start_time: float) -> str:
    """
    Calculate elapsed time and return as a human-readable string.

    :param start_time: Epoch time when task started
    :return: Formatted string of duration
    """
    elapsed = time.time() - start_time
    return f"{elapsed:.2f} seconds"