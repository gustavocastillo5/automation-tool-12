from typing import Tuple, Union

def validate_coordinates(x: int, y: int, max_width: int = 1920, max_height: int = 1080) -> Tuple[int, int]:
    """
    Validates screen coordinates to ensure they are within the screen boundaries.

    Args:
        x (int): The X coordinate.
        y (int): The Y coordinate.
        max_width (int): Maximum screen width. Defaults to 1920.
        max_height (int): Maximum screen height. Defaults to 1080.

    Returns:
        Tuple[int, int]: The validated (x, y) coordinates.

    Raises:
        ValueError: If coordinates are out of bounds or negative.
    """
    if not (0 <= x <= max_width):
        raise ValueError(f"X coordinate {x} is out of bounds (0-{max_width})")
    if not (0 <= y <= max_height):
        raise ValueError(f"Y coordinate {y} is out of bounds (0-{max_height})")
    return x, y

def validate_interval(seconds: Union[int, float]) -> float:
    """
    Validates the click interval time.

    Args:
        seconds (Union[int, float]): Time in seconds between clicks.

    Returns:
        float: Validated interval in seconds.

    Raises:
        ValueError: If interval is less than or equal to 0.
    """
    val = float(seconds)
    if val <= 0.0:
        raise ValueError("Click interval must be a positive float greater than 0")
    return val

def validate_click_count(count: int) -> int:
    """
    Validates click count configuration. Zero represents infinite clicks.

    Args:
        count (int): Number of clicks.

    Returns:
        int: The validated click count.
    """
    # We treat any value less than 0 as 0 (infinite clicks)
    val = int(count)
    return val if val >= 0 else 0

def validate_button(button: str) -> str:
    """
    Validates the mouse button specified for clicking.

    Args:
        button (str): Mouse button name, e.g., 'left', 'right', 'middle'.

    Returns:
        str: Normalized lower-case button name.

    Raises:
        ValueError: If button is not valid.
    """
    normalized = button.strip().lower()
    valid_buttons = {"left", "right", "middle"}
    if normalized not in valid_buttons:
        raise ValueError(f"Invalid mouse button: '{button}'. Must be one of {valid_buttons}")
    return normalized
