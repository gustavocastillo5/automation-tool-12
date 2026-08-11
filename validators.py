import re

def validate_email(email):
    """Validate email address format."""
    email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if not email_regex.match(email):
        raise ValueError(f'Invalid email address: {email}')
    return True


def validate_integer(value):
    """Validate integer value within given range."""
    if not isinstance(value, int):
        raise ValueError(f'Expected an integer, got {type(value).__name__}')
    return True


def validate_positive_integer(value):
    """Validate that integer is positive."""
    validate_integer(value)
    if value <= 0:
        raise ValueError(f'Integer must be positive, got: {value}')
    return True


def validate_string(value):
    """Check if value is a non-empty string."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError('Value must be a non-empty string.')
    return True