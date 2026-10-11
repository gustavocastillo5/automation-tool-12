import pyautogui
import time
import random
from typing import Tuple

def perform_click(x: int, y: int, delay: float = 0.1) -> None:
    """Move mouse to coordinates and perform a click."""
    pyautogui.moveTo(x, y)
    time.sleep(delay)
    pyautogui.click()

def get_random_delay(min_sec: float, max_sec: float) -> float:
    """Return a random float between min and max seconds."""
    return random.uniform(min_sec, max_sec)

def safe_move_and_click(x: int, y: int, jitter: int = 2) -> None:
    """Perform click with slight coordinate jitter to mimic human input."""
    target_x = x + random.randint(-jitter, jitter)
    target_y = y + random.randint(-jitter, jitter)
    pyautogui.click(x=target_x, y=target_y)

def screen_resolution() -> Tuple[int, int]:
    """Return current screen width and height."""
    return pyautogui.size()

def emergency_stop() -> None:
    """Fail-safe trigger to disable automation loop."""
    pyautogui.FAILSAFE = True