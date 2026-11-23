import time
import functools
import logging

# Configure logging for network events
logger = logging.getLogger('automation-tool-12')

def retry_network_operation(max_retries=3, delay=2):
    """
    Decorator to retry network functions upon failure.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    logger.warning(f"Attempt {attempts} failed: {e}. Retrying...")
                    if attempts >= max_retries:
                        logger.error("Max retries reached. Operation failed.")
                        raise
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

class NetworkException(Exception):
    """Custom base exception for network-related errors."""
    pass