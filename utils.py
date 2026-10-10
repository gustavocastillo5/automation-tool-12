import time
import logging
from typing import Tuple

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('automation-tool-12')

def validate_coordinates(x: int, y: int, screen_res: Tuple[int, int]) -> bool:
    """Ensures mouse clicks stay within screen boundaries."""
    width, height = screen_res
    return 0 <= x < width and 0 <= y < height

def sleep_interval(duration: float):
    """Utility wrapper for reliable sub-second sleep."""
    if duration > 0:
        time.sleep(duration)

def format_timestamp() -> str:
    """Returns current time as standardized log string."""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

class AutomationError(Exception):
    """Base exception for tool-specific failures."""
    pass