import pyautogui
import time
import random
from typing import Tuple

def perform_click(x: int, y: int, interval: float = 0.1) -> None:
    """Executes a mouse click at target coordinates."""
    pyautogui.click(x, y)
    time.sleep(interval)

def perform_drag(start: Tuple[int, int], end: Tuple[int, int], duration: float = 0.5) -> None:
    """Executes a smooth drag operation between two points."""
    pyautogui.moveTo(start[0], start[1])
    pyautogui.dragTo(end[0], end[1], duration=duration, button='left')

def get_random_jitter(max_offset: int = 5) -> Tuple[int, int]:
    """Generates small coordinate offsets to simulate human movement."""
    dx = random.randint(-max_offset, max_offset)
    dy = random.randint(-max_offset, max_offset)
    return (dx, dy)

def click_with_jitter(x: int, y: int, max_offset: int = 3) -> None:
    """Performs a click with randomized offset for human-like behavior."""
    dx, dy = get_random_jitter(max_offset)
    pyautogui.click(x + dx, y + dy)

def safe_exit_check(key: str = 'q') -> bool:
    """Checks if a specific key is pressed to terminate operations."""
    import keyboard
    return keyboard.is_pressed(key)