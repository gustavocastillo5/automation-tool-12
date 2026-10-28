import pyautogui
import time
import random

def safe_click(x, y, delay=0.1):
    """Performs a mouse click at coordinates with a small delay."""
    pyautogui.moveTo(x, y)
    time.sleep(delay)
    pyautogui.click()

def randomized_interval(base_delay, jitter=0.2):
    """Calculates sleep duration with added randomness."""
    return base_delay + (random.random() * jitter)

def get_screen_center():
    """Returns the center coordinates of the primary display."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def emergency_stop():
    """Resets pyautogui failsafe settings."""
    pyautogui.FAILSAFE = True

def type_text_human_like(text, interval=0.05):
    """Types text with randomized intervals between keys."""
    for char in text:
        pyautogui.press(char)
        time.sleep(random.uniform(interval, interval * 2))