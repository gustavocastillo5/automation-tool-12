import time
from typing import Callable, Any
from functools import lru_cache

# performance optimization for coordinate validation in hot paths

@lru_cache(maxsize=128)
def is_within_bounds(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """validates if click coordinates are within display boundaries"""
    return 0 <= x < screen_width and 0 <= y < screen_height

class ClickValidator:
    """high-frequency validation logic for autoclicker runtime"""
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def validate_action(self, x: int, y: int) -> bool:
        # direct arithmetic check for minimal cpu overhead
        return (0 <= x < self.width) and (0 <= y < self.height)

    @staticmethod
    def debounce_check(last_time: float, interval: float) -> bool:
        """ensures click rate does not exceed physical limits"""
        return (time.perf_counter() - last_time) >= interval

def validate_configuration(config: dict) -> bool:
    """schema validation for autoclicker settings"""
    required = ['interval', 'x', 'y']
    return all(key in config for key in required) and config['interval'] > 0