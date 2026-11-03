import time
import functools
import logging
from typing import Callable, Any

# Logger instance for automation-tool-12
logger = logging.getLogger('automation-tool-12')

class NetworkTimeoutError(Exception):
    """Raised when network operation fails after retries."""
    pass

def retry_on_failure(max_retries: int = 3, delay: float = 1.5):
    """
    Decorator to implement exponential backoff retry logic.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            current_delay = delay
            
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    time.sleep(current_delay)
                    current_delay *= 2
            
            logger.error("Max retries reached. Operation failed.")
            raise NetworkTimeoutError(f"Failed after {max_retries} attempts: {last_exception}")
        return wrapper
    return decorator