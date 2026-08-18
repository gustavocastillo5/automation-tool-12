from typing import List, Tuple


def calculate_click_interval(interval: float, count: int) -> List[float]:
    """
    Calculate a list of click intervals based on the total interval and count.
    
    Args:
        interval (float): Total time in seconds for the clicks.
        count (int): Number of clicks to be performed.
    
    Returns:
        List[float]: A list of intervals for each click.
    """
    if count <= 0:
        raise ValueError('Count must be greater than zero.')
    return [interval / count] * count


def generate_click_positions(screen_size: Tuple[int, int], count: int) -> List[Tuple[int, int]]:
    """
    Generate random click positions within the screen size.
    
    Args:
        screen_size (Tuple[int, int]): Width and height of the screen.
        count (int): Number of positions to generate.
    
    Returns:
        List[Tuple[int, int]]: A list of (x, y) positions for clicks.
    """
    import random
    return [(random.randint(0, screen_size[0]), random.randint(0, screen_size[1])) for _ in range(count)]


def validate_click_count(count: int) -> None:
    """
    Validate that the click count is a positive integer.
    
    Args:
        count (int): Click count to validate.
    
    Raises:
        ValueError: If the count is not valid.
    """
    if not isinstance(count, int) or count <= 0:
        raise ValueError('Click count must be a positive integer.')
