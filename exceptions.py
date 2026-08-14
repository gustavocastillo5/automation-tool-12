import time
import requests

class NetworkError(Exception):
    """Custom exception for network-related errors."""
    pass

class Retry:
    def __init__(self, retries=3, delay=1, backoff=2):
        self.retries = retries
        self.delay = delay
        self.backoff = backoff

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < self.retries:
                try:
                    return func(*args, **kwargs)
                except (requests.ConnectionError, requests.Timeout) as e:
                    attempt += 1
                    if attempt == self.retries:
                        raise NetworkError('Network operation failed after {} attempts'.format(attempt))
                    time.sleep(self.delay)
                    self.delay *= self.backoff
        return wrapper

@Retry(retries=5, delay=2)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()