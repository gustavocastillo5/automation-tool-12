import time
import pyautogui
import random

def execute_click(x, y, interval=0.1):
    """Perform a mouse click at coordinates with a small delay."""
    pyautogui.click(x, y)
    time.sleep(interval)

def execute_drag(start_x, start_y, end_x, end_y, duration=0.5):
    """Perform a drag action between two points."""
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(end_x, end_y, duration=duration, button='left')

def jitter_coordinates(x, y, range_px=5):
    """Add random noise to coordinates to avoid detection."""
    new_x = x + random.randint(-range_px, range_px)
    new_y = y + random.randint(-range_px, range_px)
    return new_x, new_y

def safe_sleep(min_sec, max_sec):
    """Sleep for a random duration to mimic human behavior."""
    duration = random.uniform(min_sec, max_sec)
    time.sleep(duration)

def perform_human_click(x, y, variation=3):
    """Execute a click with jitter for human-like interaction."""
    jx, jy = jitter_coordinates(x, y, variation)
    execute_click(jx, jy)
