import time
import random
from functools import wraps


def retry_network_operation(max_attempts: int = 3, initial_delay: float = 1.0, backoff_factor: float = 2.0):
    """
    Decorator that adds retry logic for network operations.
    Uses exponential backoff with jitter for practical use in autoclicker.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            delay = initial_delay
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError, OSError) as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        # No more retries, re-raise the last exception
                        raise
                    # Calculate next delay with backoff and random jitter
                    delay = min(delay * backoff_factor, 60)  # cap at 60 seconds
                    jitter = random.uniform(0, 0.5)
                    sleep_time = delay + jitter
                    print(f"Network operation failed (attempt {attempts}/{max_attempts}): {e}")
                    print(f"Retrying in {sleep_time:.2f} seconds...")
                    time.sleep(sleep_time)
            return None  # Unreachable but for type checkers
        return wrapper
    return decorator


# Practical example for autoclicker: retrying to send click statistics
@retry_network_operation(max_attempts=4, initial_delay=0.5, backoff_factor=1.5)
def send_click_data(click_count: int, session_id: str) -> dict:
    """
    Simulates sending data over network.
    In production, replace with actual HTTP request.
    """
    # Simulate occasional network issues
    if random.random() < 0.4:  # 40% failure rate for testing
        raise ConnectionError("Failed to connect to server")
    # Simulate successful response
    return {
        "status": "ok",
        "received_clicks": click_count,
        "session": session_id
    }


# Another example function
@retry_network_operation(max_attempts=3, initial_delay=2.0)
def check_for_updates() -> bool:
    """
    Simulate checking for tool updates.
    """
    if random.random() < 0.2:
        raise TimeoutError("Update server timeout")
    return True


if __name__ == "__main__":
    # Demo the retry logic
    try:
        result = send_click_data(150, "abc123")
        print("Success:", result)
    except Exception as e:
        print("All retries failed:", e)

    try:
        has_update = check_for_updates()
        print("Update available:", has_update)
    except Exception as e:
        print("Update check failed after retries:", e)
