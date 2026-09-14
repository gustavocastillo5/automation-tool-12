import time
import pyautogui
import random

def click_at_position(x, y, interval=0.1):
    """Perform a mouse click at specific coordinates."""
    pyautogui.click(x, y)
    time.sleep(interval)

def random_jitter(x, y, radius=5):
    """Apply minor randomness to coordinates for human-like behavior."""
    new_x = x + random.randint(-radius, radius)
    new_y = y + random.randint(-radius, radius)
    return new_x, new_y

def safe_exit_check(key='q'):
    """Check for emergency stop trigger."""
    import keyboard
    return keyboard.is_pressed(key)

def wait_random_delay(min_sec=0.5, max_sec=2.0):
    """Pause execution for a random duration to mimic user."""
    time.sleep(random.uniform(min_sec, max_sec))

def get_screen_center():
    """Retrieve coordinates for the center of the display."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def perform_drag(start_x, start_y, end_x, end_y, duration=0.5):
    """Execute a drag operation between two points."""
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(end_x, end_y, duration=duration, button='left')
