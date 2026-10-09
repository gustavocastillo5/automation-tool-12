import pyautogui
import time
import random

def safe_click(x: int, y: int, interval: float = 0.1):
    """Performs a click with randomized offset to prevent detection."""
    offset_x = random.randint(-2, 2)
    offset_y = random.randint(-2, 2)
    pyautogui.click(x + offset_x, y + offset_y)
    time.sleep(interval)

def move_and_click(x: int, y: int, duration: float = 0.2):
    """Moves mouse to coordinates and clicks safely."""
    pyautogui.moveTo(x, y, duration=duration)
    safe_click(x, y)

def get_screen_center():
    """Retrieves the current center coordinates of the primary monitor."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def perform_burst(x: int, y: int, count: int, delay: float):
    """Executes a rapid sequence of clicks at a specific target."""
    for _ in range(count):
        safe_click(x, y)
        time.sleep(delay)

def validate_bounds(x: int, y: int):
    """Checks if coordinates are within screen bounds."""
    width, height = pyautogui.size()
    return 0 <= x <= width and 0 <= y <= height