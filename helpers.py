import time
import logging
from typing import Tuple

# Logging configuration for automation-tool-12
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('automation-tool-12')

def validate_coordinates(x: int, y: int, screen_size: Tuple[int, int]) -> bool:
    """Ensure mouse coordinates are within physical screen bounds."""
    width, height = screen_size
    return 0 <= x < width and 0 <= y < height

def sleep_jitter(base_seconds: float, jitter: float = 0.1) -> None:
    """Add random variance to timing to mimic human input patterns."""
    import random
    actual_sleep = base_seconds + random.uniform(-jitter, jitter)
    time.sleep(max(0, actual_sleep))

def format_execution_time(start_time: float) -> str:
    """Calculate elapsed time since start of automation sequence."""
    elapsed = time.time() - start_time
    return f"{elapsed:.2f} seconds"