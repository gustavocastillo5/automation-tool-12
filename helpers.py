import time
import random
import pyautogui

def safe_click(x: int, y: int, interval: float = 0.1):
    """Performs a mouse click with a small safety delay."""
    pyautogui.moveTo(x, y)
    time.sleep(interval)
    pyautogui.click()

def human_delay(min_sec: float = 0.5, max_sec: float = 2.0):
    """Introduces a random delay to simulate human behavior."""
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)

def get_screen_center() -> tuple:
    """Returns the center coordinates of the primary display."""
    width, height = pyautogui.size()
    return (width // 2, height // 2)

def perform_drag(start_x: int, start_y: int, end_x: int, end_y: int):
    """Drags the mouse between two points."""
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(end_x, end_y, duration=0.5)

def validate_coordinates(x: int, y: int) -> bool:
    """Checks if coordinates are within screen boundaries."""
    width, height = pyautogui.size()
    return 0 <= x <= width and 0 <= y <= height