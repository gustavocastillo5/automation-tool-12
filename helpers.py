import time
import random
import pyautogui

def perform_click(x, y, interval=0.1):
    """Move mouse to coordinates and perform a click."""
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(interval)

def random_delay(min_ms=100, max_ms=500):
    """Wait for a randomized duration to simulate human input."""
    delay = random.uniform(min_ms, max_ms) / 1000
    time.sleep(delay)

def get_screen_center():
    """Retrieve the center coordinates of the primary monitor."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def safe_exit():
    """Emergency stop for the automation process."""
    pyautogui.FAILSAFE = True
    print("Failsafe enabled. Move mouse to screen corner to abort.")

def validate_coordinates(x, y):
    """Check if coordinates are within screen boundaries."""
    width, height = pyautogui.size()
    return 0 <= x <= width and 0 <= y <= height