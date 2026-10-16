import time
import pyautogui
from typing import Tuple, Optional

def perform_click(x: int, y: int, interval: float = 0.1) -> bool:
    """
    Executes a mouse click at specified coordinates with a delay.
    
    Args:
        x: The horizontal screen coordinate.
        y: The vertical screen coordinate.
        interval: Time to wait after clicking.
        
    Returns:
        bool: True if click was successful, False otherwise.
    """
    try:
        pyautogui.click(x=x, y=y)
        time.sleep(interval)
        return True
    except pyautogui.FailSafeException:
        return False

def get_screen_center() -> Tuple[int, int]:
    """
    Calculates the center point of the primary display.
    
    Returns:
        Tuple[int, int]: X and Y coordinates of the screen center.
    """
    width, height = pyautogui.size()
    return (width // 2, height // 2)

def validate_coordinates(x: int, y: int) -> bool:
    """
    Checks if coordinates are within current screen bounds.
    
    Args:
        x: X coordinate to validate.
        y: Y coordinate to validate.
        
    Returns:
        bool: True if valid, False if outside bounds.
    """
    width, height = pyautogui.size()
    return 0 <= x < width and 0 <= y < height