from typing import Union, Tuple

def validate_coordinates(x: int, y: int) -> bool:
    """
    Checks if coordinates fall within typical screen bounds.
    
    Args:
        x: The horizontal screen position.
        y: The vertical screen position.
        
    Returns:
        bool: True if coordinates are non-negative.
    """
    return x >= 0 and y >= 0

def validate_interval(interval: Union[int, float]) -> bool:
    """
    Validates that the click interval is a positive value.
    
    Args:
        interval: The time delay between clicks in seconds.
        
    Returns:
        bool: True if interval is greater than zero.
    """
    return interval > 0

def validate_click_count(count: int) -> bool:
    """
    Ensures the requested click count is valid.
    
    Args:
        count: Total number of clicks to perform.
        
    Returns:
        bool: True if count is non-negative.
    """
    return count >= 0

def validate_hotkey(key: str) -> bool:
    """
    Validates that the provided hotkey string is not empty.
    
    Args:
        key: The string representation of the trigger key.
        
    Returns:
        bool: True if the key is valid.
    """
    return isinstance(key, str) and len(key) > 0