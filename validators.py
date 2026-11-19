from typing import Union, Tuple

def validate_coordinates(x: int, y: int) -> bool:
    """Verify that screen coordinates are within non-negative bounds."""
    return isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0

def validate_interval(interval: float) -> bool:
    """Ensure the click interval is a positive floating point value."""
    return isinstance(interval, (int, float)) and interval > 0

def validate_button(button: str) -> bool:
    """Check if the provided mouse button name is supported."""
    supported = ('left', 'right', 'middle')
    return isinstance(button, str) and button.lower() in supported

def parse_click_data(raw_data: Tuple[int, int, float]) -> dict:
    """Transform raw tuple data into a validated dictionary format."""
    x, y, interval = raw_data
    if not (validate_coordinates(x, y) and validate_interval(interval)):
        raise ValueError("Invalid click parameters provided")
    
    return {
        "x": x,
        "y": y,
        "interval": float(interval)
    }