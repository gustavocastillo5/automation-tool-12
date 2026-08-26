import time
import functools
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-12')

def retry_operation(retries=3, delay=2, backoff=2):
    """Decorator to retry network or unstable operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    if attempt == retries:
                        logger.error(f"Operation '{func.__name__}' failed after {retries} attempts. Error: {e}")
                        raise
                    logger.warning(f"Attempt {attempt} for '{func.__name__}' failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_operation(retries=3, delay=1)
pytget_mock_request():
    """Example network operation function for the autoclicker remote sync."""
    import random
    if random.random() < 0.7:
        raise ConnectionError("Network unstable")
    return "Success"
