import time
import pyautogui
import random

def safe_click(x: int, y: int, delay_range: tuple = (0.1, 0.5)) -> None:
    """Move mouse to coordinates and perform a click with randomized delay."""
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(random.uniform(*delay_range))

def get_screen_center() -> tuple:
    """Return the center coordinates of the primary display."""
    width, height = pyautogui.size()
    return (width // 2, height // 2)

def perform_sequence(coordinates: list, interval: float = 1.0) -> None:
    """Execute clicks at a list of provided (x, y) tuples."""
    for x, y in coordinates:
        pyautogui.click(x, y)
        time.sleep(interval)

def wait_for_ready(seconds: int = 3) -> None:
    """Cooldown period before automation starts."""
    print(f"Starting in {seconds} seconds...")
    time.sleep(seconds)

def is_on_screen(x: int, y: int) -> bool:
    """Validate if coordinate is within current monitor bounds."""
    width, height = pyautogui.size()
    return 0 <= x < width and 0 <= y < height