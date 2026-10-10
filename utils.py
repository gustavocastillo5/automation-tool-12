import time
import logging
from typing import Tuple

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('automation-tool-12')

def validate_coordinates(x: int, y: int) -> bool:
    """Ensures mouse coordinates are within typical screen bounds."""
    return 0 <= x <= 3840 and 0 <= y <= 2160

def sleep_interval(duration: float) -> None:
    """Uniform sleep wrapper to throttle click frequency."""
    if duration > 0:
        time.sleep(duration)

def format_click_log(x: int, y: int, action: str) -> str:
    """Generates consistent log string for click events."""
    return f"Action: {action} at position ({x}, {y})"