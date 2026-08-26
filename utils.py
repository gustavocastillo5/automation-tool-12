import time
import functools
import logging

logger = logging.getLogger("autoclicker.utils")

def retry_network_operation(max_retries=3, delay=1.0, backoff=2.0):
    """
    Decorator to implement exponential backoff retry logic for network operations.
    Useful for auto-clicker cloud sync and license verification.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    logger.debug(f"Executing {func.__name__} (attempt {attempt}/{max_retries})")
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries:
                        logger.error(f"Operation {func.__name__} failed after {max_retries} attempts: {e}")
                        raise
                    
                    logger.warning(f"Operation {func.__name__} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

@retry_network_operation(max_retries=3, delay=0.5)
def ping_remote_server(url: str) -> bool:
    """
    Simulates a network check for the automation tool backend.
    """
    import urllib.request
    try:
        conn = urllib.request.urlopen(url, timeout=2)
        return conn.getcode() == 200
    except Exception as err:
        raise ConnectionError(f"Failed to reach {url}: {err}")
