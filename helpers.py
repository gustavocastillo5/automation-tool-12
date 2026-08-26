import time
import random

def random_delay(min_seconds: float = 0.05, max_seconds: float = 0.15) -> None:
    """Sleep for a random duration to simulate human-like behavior."""
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)

def clamp(value: int, min_val: int, max_val: int) -> int:
    """Restrict a value to be within a specified range."""
    return max(min_val, min(value, max_val))

def format_coordinates(x: int, y: int) -> str:
    """Format screen coordinates for logging and debugging."""
    return f"X: {x}, Y: {y}"

def calculate_distance(x1: int, y1: int, x2: int, y2: int) -> float:
    """Calculate Euclidean distance between two points."""
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
