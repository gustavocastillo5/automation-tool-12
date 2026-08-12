import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, max_retries=3, delay=2):
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad HTTP status
            return response.json()  # Return the JSON response if successful
        except requests.RequestException as e:
            attempts += 1
            print(f"Attempt {attempts} failed: {e}")
            if attempts < max_retries:
                time.sleep(delay)  # Wait before retrying
            else:
                raise NetworkError(f"Failed to fetch {url} after {max_retries} attempts")

# Example usage:
# data = retry_request('https://api.example.com/data')
# print(data)  
