import random
import time
from typing import Tuple


def calculate_jitter_delay(base_interval: float, jitter: float) -> float:
    """Calculate a randomized delay interval to simulate human clicking variance."""
    if base_interval <= 0:
        return 0.0
    variance = base_interval * max(0.0, min(jitter, 1.0))
    delay = base_interval + random.uniform(-variance, variance)
    return max(0.001, delay)


def cps_to_interval(cps: float) -> float:
    """Convert clicks per second (CPS) to time interval in seconds."""
    if cps <= 0:
        raise ValueError("Clicks per second must be greater than zero.")
    return 1.0 / cps


def clamp_coordinates(
    x: int, y: int, screen_bounds: Tuple[int, int, int, int]
) -> Tuple[int, int]:
    """Ensure target click coordinates stay within specified screen boundaries."""
    min_x, min_y, max_x, max_y = screen_bounds
    clamped_x = max(min_x, min(x, max_x))
    clamped_y = max(min_y, min(y, max_y))
    return clamped_x, clamped_y


def format_click_stats(total_clicks: int, elapsed_time: float) -> str:
    """Format click execution statistics into a readable string summary."""
    if elapsed_time <= 0:
        return f"Total clicks: {total_clicks} | Avg CPS: 0.0"
    avg_cps = total_clicks / elapsed_time
    return (
        f"Total clicks: {total_clicks} | Time: {elapsed_time:.2f}s | "
        f"Avg CPS: {avg_cps:.1f}"
    )
