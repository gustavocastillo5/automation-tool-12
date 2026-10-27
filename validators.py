from typing import Dict, Any, Tuple


class ValidationError(Exception):
    """Raised when click processing inputs fail validation checks."""
    pass


def validate_coordinates(coords: Any, screen_size: Tuple[int, int] = (3840, 2160)) -> Tuple[int, int]:
    """Validate target x, y click coordinates against allowable screen bounds."""
    if not isinstance(coords, (tuple, list)) or len(coords) != 2:
        raise ValidationError("Coordinates must be a tuple or list of 2 integers (x, y).")
    
    x, y = coords
    if not (isinstance(x, int) and isinstance(y, int)):
        raise ValidationError("Coordinate values x and y must be integers.")
        
    max_x, max_y = screen_size
    if not (0 <= x <= max_x and 0 <= y <= max_y):
        raise ValidationError(f"Coordinates ({x}, {y}) are outside screen bounds (0-{max_x}, 0-{max_y}).")
        
    return x, y


def validate_click_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """Validate user parameters before starting the main click loop."""
    required_keys = {"coords", "interval", "button", "repeat_count"}
    missing = required_keys - set(config.keys())
    if missing:
        raise ValidationError(f"Missing required parameters in processing payload: {', '.join(missing)}")

    validate_coordinates(config["coords"])

    interval = config["interval"]
    if not isinstance(interval, (int, float)) or interval < 0.001:
        raise ValidationError("Click interval must be a number greater than or equal to 0.001s.")

    valid_buttons = {"left", "right", "middle", "double"}
    if config["button"] not in valid_buttons:
        raise ValidationError(f"Invalid mouse button '{config['button']}'. Must be one of: {valid_buttons}")

    repeat_count = config["repeat_count"]
    if not isinstance(repeat_count, int) or repeat_count < -1:
        raise ValidationError("Repeat count must be an integer >= -1 (-1 indicates continuous loop).")

    return config
