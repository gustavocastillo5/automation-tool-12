import time
import requests
from requests.exceptions import RequestException

def validate_url(url):
    if not isinstance(url, str):
        raise ValueError('URL must be a string')
    if not url.startswith(('http://', 'https://')):
        raise ValueError('Invalid URL format')

def retry_request(url, retries=3, delay=1):
    validate_url(url)
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()  # Assuming the response is JSON
        except RequestException as e:
            if attempt < retries - 1:
                time.sleep(delay)  # Wait before retrying
                continue
            else:
                raise e  # Raise the last exception if retries are exhausted