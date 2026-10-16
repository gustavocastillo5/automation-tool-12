import functools
import logging
import time
from typing import Any, Callable, Tuple, Type

logger = logging.getLogger(__name__)


def retry_on_exception(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,)
) -> Callable:
    """
    Decorator that retries a function if specified exceptions occur.
    Applies exponential backoff delay between retry attempts.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        logger.error(
                            "Operation '%s' failed after %d retries. Error: %s",
                            func.__name__, max_retries, err
                        )
                        raise
                    
                    logger.warning(
                        "Attempt %d/%d for '%s' failed (%s). Retrying in %.1fs...",
                        attempt, max_retries, func.__name__, err, current_delay
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None

        return wrapper
    return decorator


def execute_with_retry(
    func: Callable,
    *args: Any,
    max_retries: int = 3,
    delay: float = 1.0,
    **kwargs: Any
) -> Any:
    """Helper function to execute a callable directly with retry logic."""
    retry_wrapper = retry_on_exception(max_retries=max_retries, delay=delay)
    return retry_wrapper(func)(*args, **kwargs)
