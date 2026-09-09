import time
import logging
from typing import Tuple

# Configure basic logging for automation events
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('automation-tool-12')

def validate_coordinates(x: int, y: int, screen_size: Tuple[int, int]) -> bool:
    """Ensures click targets remain within display boundaries."""
    width, height = screen_size
    return 0 <= x <= width and 0 <= y <= height

def sleep_interval(duration: float):
    """Standardized sleep wrapper for anti-detection timing."""
    if duration > 0:
        time.sleep(duration)

def format_log_entry(action: str, x: int, y: int) -> str:
    """Generates consistent log strings for click history."""
    return f"Action: {action} at position ({x}, {y})"

def calculate_jitter(base_val: int, intensity: int = 5) -> int:
    """Adds randomization to mouse positioning to simulate human input."""
    import random
    return base_val + random.randint(-intensity, intensity)