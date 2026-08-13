import time
import requests
from requests.exceptions import RequestException

class NetworkHandler:
    def __init__(self, max_retries=3, backoff_factor=0.5):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def send_request(self, url):
        retries = 0
        while retries < self.max_retries:
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise an error for bad responses
                return response.json()  # Return the JSON content of the response
            except RequestException as e:
                retries += 1
                wait_time = self.backoff_factor * (2 ** retries)  # Exponential backoff
                print(f'Error occurred: {e}. Retrying in {wait_time:.2f} seconds...')
                time.sleep(wait_time)
        raise ConnectionError(f'Failed to connect to {url} after {self.max_retries} retries.')