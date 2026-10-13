import time
import pyautogui
from typing import Tuple

def move_and_click(x: int, y: int, button: str = 'left') -> None:
    """Move mouse to coordinates and perform a click."""
    pyautogui.moveTo(x, y)
    pyautogui.click(button=button)

def get_mouse_position() -> Tuple[int, int]:
    """Return current (x, y) coordinates of mouse."""
    return pyautogui.position()

def safe_sleep(seconds: float) -> None:
    """Pause execution for the specified duration."""
    if seconds > 0:
        time.sleep(seconds)

def check_screen_pixel(x: int, y: int, color: Tuple[int, int, int]) -> bool:
    """Verify pixel color at specific coordinates."""
    return pyautogui.pixelMatchesColor(x, y, color)

def drag_to_location(x1: int, y1: int, x2: int, y2: int, duration: float = 0.5) -> None:
    """Drag item from first coordinate to second."""
    pyautogui.moveTo(x1, y1)
    pyautogui.dragTo(x2, y2, duration=duration)