import time
import functools
import logging
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger("autoclicker.utils")

def retry_network_op(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,)
) -> Callable:
    """
    Decorator that retries network operations with exponential backoff.

    :param max_retries: Maximum number of retry attempts allowed.
    :param initial_delay: Initial delay between attempts in seconds.
    :param backoff_factor: Multiplier for calculating the next delay.
    :param exceptions: Tuple of exception types that trigger a retry.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = initial_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        logger.error(
                            f"Operation '{func.__name__}' failed after {max_retries} attempts: {err}"
                        )
                        raise

                    logger.warning(
                        f"Network operation '{func.__name__}' failed (attempt {attempt}/{max_retries}). "
                        f"Retrying in {current_delay:.2f}s... Error: {err}"
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff_factor
        return wrapper
    return decorator