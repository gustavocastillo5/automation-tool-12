import time
import logging
from functools import wraps
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger("automation_tool.utils")

def retry(
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    tries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0
) -> Callable:
    """
    Decorator that retries a function call with exponential backoff.
    
    :param exceptions: A tuple of exceptions to catch.
    :param tries: Total number of execution attempts.
    :param delay: Initial delay between retries in seconds.
    :param backoff: Multiplier applied to delay after each failure.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt_delay = delay
            for attempt in range(1, tries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == tries:
                        logger.error(f"Failed '{func.__name__}' after {tries} attempts due to: {e}")
                        raise
                    logger.warning(
                        f"Retrying '{func.__name__}' in {attempt_delay:.2f} seconds... "
                        f"(Attempt {attempt}/{tries}) due to error: {e}"
                    )
                    time.sleep(attempt_delay)
                    attempt_delay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator