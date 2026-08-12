import time
import random

class ClickError(Exception):
    """Custom exception for click handling errors."""
    pass


def simulate_click(position):
    try:
        if not isinstance(position, (tuple, list)) or len(position) != 2:
            raise ClickError("Position must be a tuple or list with two elements.")

        x, y = position
        if not (isinstance(x, int) and isinstance(y, int)):
            raise ClickError("Coordinates must be integers.")

        # Simulating a click (placeholder for actual click functionality)
        print(f"Clicking at position: {position}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate the delay before the next click
    except ClickError as e:
        print(f"Error while simulating click: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def click_multiple_times(position, times):
    try:
        if not isinstance(times, int) or times <= 0:
            raise ClickError("'times' must be a positive integer.")

        for _ in range(times):
            simulate_click(position)
    except ClickError as e:
        print(f"Error in click_multiple_times: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during multiple clicks: {e}")


if __name__ == '__main__':
    click_multiple_times((500, 300), 5)  # Example usage
