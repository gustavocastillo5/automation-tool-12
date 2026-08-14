import re

def is_valid_click_coordinate(value):
    """
    Validates if the input coordinate is a tuple of two integers.
    """
    if isinstance(value, tuple) and len(value) == 2:
        return all(isinstance(coord, int) for coord in value)
    return False


def is_valid_click_interval(value):
    """
    Validates if the input click interval is a positive integer.
    """
    return isinstance(value, int) and value > 0


def is_valid_click_count(value):
    """
    Validates if the number of clicks is a positive integer.
    """
    return isinstance(value, int) and value > 0


if __name__ == '__main__':
    # Test cases
    print(is_valid_click_coordinate((100, 200)))  # True
    print(is_valid_click_coordinate((100,)))       # False
    print(is_valid_click_interval(500))             # True
    print(is_valid_click_interval(-10))             # False
    print(is_valid_click_count(10))                 # True
    print(is_valid_click_count(0))                  # False