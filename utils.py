import time
import logging
from functools import wraps
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger("autoclicker.utils")

def retry_network_op(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,)
) -> Callable:
    """
    Decorator that retries network operations with exponential backoff.
    Useful for fetching remote autoclicker presets or checking license keys.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    if attempt == max_retries:
                        logger.error(
                            f"Network call '{func.__name__}' failed after {max_retries} attempts: {exc}"
                        )
                        raise
                    
                    logger.warning(
                        f"Attempt {attempt}/{max_retries} for '{func.__name__}' failed: {exc}. "
                        f"Retrying in {current_delay:.2f}s..."
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff_factor
        return wrapper
    return decorator
