"""Helper functions for automation tool autoclicker"""

import time
import random
import pyautogui
from typing import Tuple

# Enable failsafe to stop script on mouse to corner
pyautogui.FAILSAFE = True

def random_delay(min_sec: float = 0.1, max_sec: float = 0.5) -> None:
    """Pause execution for a random time interval"""
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)

def move_to_and_click(x: int, y: int, clicks: int = 1) -> None:
    """Relocate mouse cursor then execute click"""
    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.click(clicks=clicks)

def random_position_in_bounds() -> Tuple[int, int]:
    """Select random coordinates on current screen"""
    width, height = pyautogui.size()
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    return x, y

def click_at_random() -> None:
    """Perform a click at random screen location"""
    x, y = random_position_in_bounds()
    move_to_and_click(x, y)

def delayed_click(x: int, y: int, min_delay: float = 0.05) -> None:
    """Add delay before clicking at coordinates"""
    random_delay(min_delay, min_delay + 0.3)
    move_to_and_click(x, y)

def get_current_mouse_pos() -> Tuple[int, int]:
    """Retrieve present mouse cursor location"""
    return pyautogui.position()

def check_bounds(x: int, y: int) -> bool:
    """Verify if given coordinates are on screen"""
    width, height = pyautogui.size()
    return 0 <= x < width and 0 <= y < height

def safe_move_and_click(x: int, y: int) -> bool:
    """Click only after confirming position validity"""
    if check_bounds(x, y):
        move_to_and_click(x, y)
        return True
    return False

def multi_click(x: int, y: int, count: int, interval: float = 0.1) -> None:
    """Execute multiple clicks with fixed interval"""
    for _ in range(count):
        move_to_and_click(x, y)
        random_delay(0, interval)