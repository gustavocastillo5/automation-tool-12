import time
import logging
import requests
from functools import wraps

logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts=3, delay=2):
    """Decorator for retrying network operations on failure."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.RequestException, ConnectionError) as e:
                    attempts += 1
                    logger.warning(f"Attempt {attempts} failed: {e}")
                    if attempts >= max_attempts:
                        logger.error("Max retries reached. Operation failed.")
                        raise
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry_network_operation(max_attempts=3, delay=1)
def send_click_event(endpoint, payload):
    """Sends click coordinates to the remote automation server."""
    response = requests.post(endpoint, json=payload, timeout=5)
    response.raise_for_status()
    return response.json()