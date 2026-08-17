import re

def validate_input(input_value):
    """
    Validate the user input to ensure it meets the required criteria.
    The input should be a positive integer and within a specified range.
    """
    try:
        value = int(input_value)
        if value <= 0:
            raise ValueError("Input must be a positive integer.")
        return value
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None


def validate_coordinates(x, y):
    """
    Validate the coordinates to ensure they are within screen bounds.
    The coordinates should be non-negative integers.
    """
    if not (isinstance(x, int) and isinstance(y, int)):
        print("Coordinates must be integers.")
        return False
    if x < 0 or y < 0:
        print("Coordinates must be non-negative.")
        return False
    return True


# Example usage in main processing loop:
if __name__ == '__main__':
    user_input = input("Enter a positive integer: ")
    validated_input = validate_input(user_input)
    if validated_input is not None:
        print(f"Valid input: {validated_input}")
    x_coord = -1  # example coordinate
    y_coord = 100
    if validate_coordinates(x_coord, y_coord):
        print("Coordinates are valid.")
    else:
        print("Invalid coordinates.")