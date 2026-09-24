import time
import functools
import logging

# Setup basic logger for automation-tool-12
logger = logging.getLogger('automation-tool-12')

def retry(max_attempts=3, delay=2, backoff=2):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f'Operation failed after {max_attempts} attempts')
                        raise e
                    logger.warning(f'Attempt {attempts} failed, retrying in {current_delay}s...')
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

@retry(max_attempts=3, delay=1)
def perform_network_request(url):
    """Example function to be decorated with retry logic."""
    # Simulating a network request
    return True