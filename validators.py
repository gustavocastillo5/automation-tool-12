import time
import functools
import logging

# Setup basic logger for automation-tool-12
logger = logging.getLogger('automation-tool-12')

def retry_network_operation(retries=3, delay=2, exceptions=(ConnectionError, TimeoutError)):
    """
    Decorator to retry network-bound operations upon failure.
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
            
            logger.error(f"Operation {func.__name__} failed after {retries} attempts.")
            raise last_exception
        return wrapper
    return decorator

@retry_network_operation(retries=3, delay=1)
def validate_server_connection(endpoint):
    """
    Sample network validation using retry decorator.
    """
    # In a real scenario, this performs an actual request
    return True