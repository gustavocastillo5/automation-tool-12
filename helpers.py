import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_op(retries=3, delay=2, exceptions=(ConnectionError, TimeoutError)):
    """
    Decorator to retry network operations upon specific exceptions.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            
            logger.error("Max retries exceeded for network operation.")
            raise last_exception
        return wrapper
    return decorator

@retry_network_op(retries=3, delay=1)
def fetch_remote_config(url):
    """
    Example network-bound function for the autoclicker remote settings.
    """
    # Placeholder for actual requests call logic
    import random
    if random.random() < 0.7:
        raise ConnectionError("Failed to reach configuration server")
    return {"status": "ok", "interval": 0.5}