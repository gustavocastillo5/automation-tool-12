import time
import pyautogui
import random

def click_at(x, y, interval=0.1):
    """Performs a click with a slight randomized delay."""
    pyautogui.moveTo(x, y)
    time.sleep(random.uniform(0.01, interval))
    pyautogui.click()

def safe_move(x, y, duration=0.2):
    """Moves mouse to coordinates with a set duration."""
    pyautogui.moveTo(x, y, duration=duration, tween=pyautogui.easeInOutQuad)

def wait_for_seconds(base_seconds, variance=0.5):
    """Pauses execution for a random duration around a base."""
    sleep_time = base_seconds + random.uniform(-variance, variance)
    time.sleep(max(0, sleep_time))

def get_screen_center():
    """Returns the center coordinates of the primary monitor."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def perform_double_click(x, y):
    """Performs a double click at the target coordinates."""
    pyautogui.doubleClick(x, y)

def drag_to(start_x, start_y, end_x, end_y):
    """Drags mouse from start to end coordinates."""
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(end_x, end_y, duration=0.5, button='left')
