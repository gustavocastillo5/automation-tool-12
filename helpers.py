import pyautogui
import time
import random

def perform_click(x: int, y: int, interval: float = 0.05):
    """Move mouse to coordinates and execute click."""
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(interval)

def random_jitter(x: int, y: int, range_px: int = 5) -> tuple:
    """Add random noise to coordinates for human-like movement."""
    dx = random.randint(-range_px, range_px)
    dy = random.randint(-range_px, range_px)
    return (x + dx, y + dy)

def safe_exit_check(key: str = 'q') -> bool:
    """Check if user requested program termination."""
    if pyautogui.getActiveWindow() and pyautogui.key_down(key):
        return True
    return False

def human_delay(min_sec: float = 0.1, max_sec: float = 0.5):
    """Sleep for a random duration to simulate human reaction."""
    time.sleep(random.uniform(min_sec, max_sec))

def get_screen_size() -> tuple:
    """Return tuple of current display resolution."""
    return pyautogui.size()