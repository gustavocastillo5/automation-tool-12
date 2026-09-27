import time
import functools
import logging

# Logger instance for automation-tool-12
logger = logging.getLogger('automation-tool-12')

def retry_on_failure(retries=3, delay=2, exceptions=(Exception,)):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying in {current_delay}s...")
                    if attempt < retries:
                        time.sleep(current_delay)
                        current_delay *= 2
            logger.error(f"Operation failed after {retries} attempts: {last_exception}")
            raise last_exception
        return wrapper
    return decorator

@retry_on_failure(retries=3, delay=1)
def validate_connection(target_url):
    """Simple check for network availability for the autoclicker."""
    import requests
    response = requests.get(target_url, timeout=5)
    return response.status_code == 200