from typing import Tuple, Dict, Any, Union

def validate_interval(interval: Union[int, float]) -> bool:
    """Validates that the click interval is a positive number (minimum 1ms)."""
    if not isinstance(interval, (int, float)):
        return False
    return interval >= 0.001

def validate_coordinates(coords: Tuple[int, int], screen_size: Tuple[int, int] = (1920, 1080)) -> bool:
    """Validates that target coordinates are within the current screen bounds."""
    if not isinstance(coords, tuple) or len(coords) != 2:
        return False
    x, y = coords
    if not (isinstance(x, int) and isinstance(y, int)):
        return False
    return 0 <= x <= screen_size[0] and 0 <= y <= screen_size[1]

def validate_button(button: str) -> bool:
    """Validates that the specified mouse button is a valid input device key."""
    if not isinstance(button, str):
        return False
    return button.lower() in {"left", "right", "middle"}

def validate_config(config: Dict[str, Any], screen_size: Tuple[int, int] = (1920, 1080)) -> Dict[str, str]:
    """
    Performs a comprehensive check on autoclicker settings.
    Returns a dictionary of found validation errors.
    """
    errors = {}
    
    # Validate Interval
    if "interval" in config:
        if not validate_interval(config["interval"]):
            errors["interval"] = "Interval must be a float or integer representing seconds >= 0.001"
    else:
        errors["interval"] = "Missing interval configuration"

    # Validate Optional Coordinates
    if config.get("coords") is not None:
        if not validate_coordinates(config["coords"], screen_size):
            errors["coords"] = f"Coordinates must be an (x, y) tuple within screen bounds {screen_size}"

    # Validate Mouse Button Selection
    if "button" in config:
        if not validate_button(config["button"]):
            errors["button"] = "Button must be one of: 'left', 'right', 'middle'"

    return errors