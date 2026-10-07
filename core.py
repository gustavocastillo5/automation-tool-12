import pyautogui
import time
import random

def safe_click(x: int, y: int, interval: float = 0.1):
    """Performs a click at specified coordinates with randomized delay."""
    pyautogui.moveTo(x, y)
    time.sleep(random.uniform(0.05, interval))
    pyautogui.click()

def drag_and_drop(start_x: int, start_y: int, end_x: int, end_y: int, duration: float = 0.5):
    """Simulates a drag motion between two points."""
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(end_x, end_y, duration=duration, button='left')

def batch_click(points: list, delay: float = 1.0):
    """Executes a sequence of clicks defined by list of tuples."""
    for x, y in points:
        safe_click(x, y)
        time.sleep(delay)

def get_screen_center():
    """Returns the center coordinates of the primary display."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def perform_double_click(x: int, y: int):
    """Performs a double click operation at screen coordinates."""
    pyautogui.doubleClick(x, y)

if __name__ == '__main__':
    # Example usage: click the center of the screen
    cx, cy = get_screen_center()
    safe_click(cx, cy)