from typing import Union, Tuple

def validate_coordinates(x: int, y: int) -> bool:
    """Verify that click coordinates are within non-negative bounds."""
    return isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0

def validate_interval(interval: float) -> bool:
    """Check if the click interval is a positive non-zero value."""
    return isinstance(interval, (int, float)) and interval > 0

def validate_button(button: str) -> bool:
    """Ensure the input button identifier is valid for mouse events."""
    valid_buttons: Tuple[str, ...] = ("left", "right", "middle")
    return button.lower() in valid_buttons

def format_click_data(x: int, y: int, interval: float) -> dict:
    """Structure validated click parameters into a dictionary object."""
    if not all([validate_coordinates(x, y), validate_interval(interval)]):
        raise ValueError("Invalid click parameters provided")
    
    return {
        "position": (x, y),
        "interval": float(interval),
        "status": "ready"
    }