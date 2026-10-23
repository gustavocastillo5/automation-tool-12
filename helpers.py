import time
import pyautogui
import random

def perform_click(x, y, interval=(0.1, 0.3)):
    """Moves mouse and performs a click with jittery delay."""
    pyautogui.moveTo(x, y)
    time.sleep(random.uniform(*interval))
    pyautogui.click()

def get_screen_bounds():
    """Returns current screen resolution dimensions."""
    return pyautogui.size()

def is_within_bounds(x, y, width, height):
    """Validates if coordinates are inside screen area."""
    return 0 <= x <= width and 0 <= y <= height

def safe_exit(message="Exiting automation tool..."):
    """Prints status and stops execution flow."""
    print(message)
    exit(0)

def random_delay(min_sec=0.5, max_sec=2.0):
    """Pauses execution for a random interval."""
    time.sleep(random.uniform(min_sec, max_sec))