from typing import Any, Dict, Union


def is_valid_email(email: str) -> bool:
    """
    Validates if the provided email address is in a correct format.

    Args:
        email (str): Email address to validate.

    Returns:
        bool: True if valid email format, else False.
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def is_valid_age(age: Union[int, float]) -> bool:
    """
    Checks if the given age is a valid positive integer or float.

    Args:
        age (Union[int, float]): Age to validate.

    Returns:
        bool: True if age is a positive number, else False.
    """
    return isinstance(age, (int, float)) and age > 0


def is_non_empty_string(value: Any) -> bool:
    """
    Checks if the provided value is a non-empty string.

    Args:
        value (Any): Value to check.

    Returns:
        bool: True if value is a non-empty string, else False.
    """
    return isinstance(value, str) and bool(value.strip())


def validate_user_info(user_info: Dict[str, Any]) -> bool:
    """
    Validates the user information dictionary.

    Args:
        user_info (Dict[str, Any]): Dictionary containing user information.

    Returns:
        bool: True if user information is valid, else False.
    """
    return (is_valid_email(user_info.get('email', '')) and
            is_valid_age(user_info.get('age', 0)) and
            is_non_empty_string(user_info.get('name', '')))