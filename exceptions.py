import time
import functools
import logging

# Configure basic logger for network events
logger = logging.getLogger('automation-tool-12')

class NetworkError(Exception):
    """Base class for network exceptions in automation-tool-12."""
    pass

def retry_on_failure(max_attempts=3, delay=2):
    """
    Decorator to retry network operations upon encountering exceptions.
    
    :param max_attempts: Maximum number of retry attempts
    :param delay: Seconds to wait between retries
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    logger.warning(f"Attempt {attempts} failed for {func.__name__}: {e}")
                    if attempts >= max_attempts:
                        logger.error(f"Max retries reached for {func.__name__}.")
                        raise NetworkError(f"Operation failed after {max_attempts} attempts.")
                    time.sleep(delay)
        return wrapper
    return decorator