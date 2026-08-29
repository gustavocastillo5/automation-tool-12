import time
import random
from typing import List, Tuple

def get_random_delay(min_delay: float, max_delay: float) -> float:
    """Generate random delay value between given min and max"""
    if min_delay > max_delay:
        min_delay, max_delay = max_delay, min_delay
    return random.uniform(min_delay, max_delay)

def apply_random_delay(min_delay: float = 0.05, max_delay: float = 0.25) -> None:
    """Pause execution for random time to mimic natural pauses"""
    delay = get_random_delay(min_delay, max_delay)
    time.sleep(delay)

def get_random_position(x: int, y: int, variance: int = 8) -> Tuple[int, int]:
    """Add small random variance to base coordinates"""
    if variance < 0:
        variance = 0
    rx = x + random.randint(-variance, variance)
    ry = y + random.randint(-variance, variance)
    return rx, ry

def check_position_valid(x: int, y: int, max_x: int = 1920, max_y: int = 1080) -> bool:
    """Verify coordinates are within screen dimensions"""
    return 0 <= x <= max_x and 0 <= y <= max_y

def build_click_list(x: int, y: int, num_clicks: int, variance: int = 8) -> List[Tuple[int, int]]:
    """Create list of positions for multiple clicks"""
    clicks: List[Tuple[int, int]] = []
    for _ in range(num_clicks):
        pos = get_random_position(x, y, variance)
        if check_position_valid(pos[0], pos[1]):
            clicks.append(pos)
    return clicks

def execute_clicks(clicks: List[Tuple[int, int]], min_d: float = 0.05, max_d: float = 0.2) -> None:
    """Iterate through clicks applying delays between each"""
    for idx, position in enumerate(clicks):
        # Actual implementation would use mouse library here
        # e.g. pyautogui.click(position[0], position[1])
        print(f"Click {idx + 1}: at {position}")  # demonstration only
        apply_random_delay(min_d, max_d)
    print("All clicks executed")

if __name__ == "__main__":
    positions = build_click_list(500, 300, 5)
    execute_clicks(positions)