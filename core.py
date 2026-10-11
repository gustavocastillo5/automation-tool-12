import time
import logging
import requests
from functools import wraps

# Configure logger for automation-tool-12
logger = logging.getLogger('automation-tool-12')

def retry_network_op(max_retries=3, delay=2):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except (requests.RequestException, ConnectionError) as e:
                    attempts += 1
                    if attempts >= max_retries:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    time.sleep(delay * attempts)
        return wrapper
    return decorator

@retry_network_op(max_retries=3, delay=1)
def fetch_config_from_server(url):
    """Simple helper to sync autoclicker configuration."""
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    # Example usage in the autoclicker context
    try:
        config = fetch_config_from_server('http://api.local/config')
        print(f"Loaded config: {config}")
    except Exception as e:
        print(f"Autoclicker initialization failed: {e}")