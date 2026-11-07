import logging
import sys
from typing import Callable, Any, Optional

logger = logging.getLogger('automation-tool-12')

def execute_with_safety(func: Callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    """Executes click events with robust boundary checks."""
    try:
        return func(*args, **kwargs)
    except PermissionError:
        logger.error("Insufficient OS privileges to perform click.")
    except ValueError as e:
        logger.error(f"Invalid coordinates provided: {e}")
    except Exception as e:
        logger.critical(f"Unexpected system failure: {e}")
    return None

def validate_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """Checks if coordinate inputs are within monitor bounds."""
    if not isinstance(x, int) or not isinstance(y, int):
        logger.warning("Non-integer coordinates received.")
        return False
    if 0 <= x <= screen_width and 0 <= y <= screen_height:
        return True
    logger.warning(f"Coordinates ({x}, {y}) out of bounds.")
    return False

def get_safe_input(prompt: str, min_val: int, max_val: int) -> int:
    """Sanitizes user input for autoclicker timing configurations."""
    try:
        value = int(input(prompt))
        return max(min_val, min(value, max_val))
    except ValueError:
        logger.warning("Invalid numeric input, defaulting to minimum.")
        return min_val