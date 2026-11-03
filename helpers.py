import time
import pyautogui
import random

def safe_click(x: int, y: int, interval: float = 0.1):
    """Move mouse to coordinates and perform a click with jitter."""
    pyautogui.moveTo(x + random.uniform(-1, 1), y + random.uniform(-1, 1), duration=0.1)
    pyautogui.click()
    time.sleep(interval)

def get_screen_center():
    """Calculate the center point of the primary display."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def wait_random(min_s: float, max_s: float):
    """Pause execution for a randomized duration."""
    time.sleep(random.uniform(min_s, max_s))

def validate_coordinates(x: int, y: int):
    """Ensure coordinates are within screen bounds."""
    width, height = pyautogui.size()
    return 0 <= x <= width and 0 <= y <= height

def perform_sequence(coords: list):
    """Execute a series of clicks from a list of tuples."""
    for x, y in coords:
        if validate_coordinates(x, y):
            safe_click(x, y)
        else:
            print(f"Warning: coordinate {x}, {y} out of bounds")