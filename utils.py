import time
import functools
import logging
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger(__name__)

def retry_network_op(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    retryable_exceptions: Tuple[Type[Exception], ...] = (Exception,)
) -> Callable:
    """
    Decorator to retry network requests with exponential backoff.
    Used for syncing autoclicker configuration profiles and online hooks.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = initial_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except retryable_exceptions as err:
                    if attempt == max_retries:
                        logger.error(
                            f"Operation '{func.__name__}' failed after {max_retries} attempts: {err}"
                        )
                        raise
                    
                    logger.warning(
                        f"Network operation '{func.__name__}' failed (Attempt {attempt}/{max_retries}): {err}. "
                        f"Retrying in {current_delay:.2f}s..."
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff_factor
        return wrapper
    return decorator
