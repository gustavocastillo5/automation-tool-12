import time
import pyautogui
from typing import Tuple

def get_mouse_position() -> Tuple[int, int]:
    """Returns the current (x, y) coordinates of the mouse."""
    return pyautogui.position()

def perform_click(x: int, y: int, interval: float = 0.1) -> None:
    """Moves to coordinates and executes a standard left click."""
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(interval)

def wait_for_seconds(seconds: float) -> None:
    """Pauses execution for a specified duration."""
    time.sleep(seconds)

def get_screen_resolution() -> Tuple[int, int]:
    """Returns the width and height of the primary display."""
    return pyautogui.size()

def safe_exit_check(key: str = 'q') -> bool:
    """Checks if the specified hotkey is pressed to stop execution."""
    try:
        import keyboard
        return keyboard.is_pressed(key)
    except ImportError:
        return False