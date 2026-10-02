import pyautogui
import time
import random

def perform_click(x, y, interval=0.1):
    """Moves mouse to coordinates and performs a click."""
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(interval)

def random_click(x_range, y_range, jitter=5):
    """Performs a click with randomized offset for human-like behavior."""
    target_x = random.randint(x_range[0], x_range[1]) + random.randint(-jitter, jitter)
    target_y = random.randint(y_range[0], y_range[1]) + random.randint(-jitter, jitter)
    perform_click(target_x, target_y)

def safe_exit_check(key='q'):
    """Checks if the exit key was pressed to stop automation."""
    if pyautogui.press(key, presses=0): 
        return True
    return False

def delay_execution(min_sec, max_sec):
    """Waits for a random duration to mimic natural usage."""
    sleep_time = random.uniform(min_sec, max_sec)
    time.sleep(sleep_time)

def get_screen_center():
    """Returns the center coordinates of the primary display."""
    width, height = pyautogui.size()
    return width // 2, height // 2