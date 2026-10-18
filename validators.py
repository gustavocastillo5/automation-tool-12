"""Validation utilities for autoclicker configuration parameters."""

from typing import Optional, Tuple, Union


def validate_cps(cps: Union[int, float]) -> float:
    """Validate clicks per second (CPS) setting.

    Args:
        cps: Target clicks per second.

    Returns:
        Validated CPS as a float.

    Raises:
        ValueError: If CPS is outside the allowed range (0.1 to 1000.0).
    """
    cps_float = float(cps)
    if not (0.1 <= cps_float <= 1000.0):
        raise ValueError("CPS must be between 0.1 and 1000.0")
    return cps_float


def validate_coordinates(
    coords: Optional[Tuple[int, int]],
    screen_bounds: Tuple[int, int] = (1920, 1080),
) -> Optional[Tuple[int, int]]:
    """Validate target screen coordinates.

    Args:
        coords: (x, y) coordinate tuple or None for dynamic cursor position.
        screen_bounds: (width, height) boundary tuple.

    Returns:
        Validated (x, y) coordinate tuple or None.

    Raises:
        ValueError: If coordinates are out of screen bounds.
    """
    if coords is None:
        return None

    x, y = coords
    max_x, max_y = screen_bounds
    if x < 0 or y < 0 or x > max_x or y > max_y:
        raise ValueError(
            f"Coordinates ({x}, {y}) out of screen bounds {screen_bounds}"
        )
    return int(x), int(y)


def validate_click_count(count: int) -> int:
    """Validate total click target count.

    Args:
        count: Number of clicks to perform (0 for infinite).

    Returns:
        Validated click count as an integer.

    Raises:
        ValueError: If count is negative.
    """
    count_int = int(count)
    if count_int < 0:
        raise ValueError("Click count cannot be negative")
    return count_int
