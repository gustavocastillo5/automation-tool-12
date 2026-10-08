import time
import random
import logging
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger("automation_tool.utils")

def retry_on_failure(
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    jitter: bool = True
) -> Callable:
    """
    Decorator that retries a function call if specific exceptions are raised.
    
    Uses exponential backoff and optional jitter to avoid thundering herd.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries:
                        logger.error(
                            f"Failed {func.__name__} after {retries} attempts. Error: {e}"
                        )
                        raise
                    
                    sleep_time = attempt_delay
                    if jitter:
                        sleep_time *= random.uniform(0.5, 1.5)
                        
                    logger.warning(
                        f"Attempt {attempt}/{retries} failed for {func.__name__}: {e}. "
                        f"Retrying in {sleep_time:.2f} seconds..."
                    )
                    time.sleep(sleep_time)
                    attempt_delay *= backoff
        return wrapper
    return decorator
