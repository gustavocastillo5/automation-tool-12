import re

def is_valid_email(email):
    """
    Validate the email format.
    Returns True if valid, otherwise False.
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None


def is_valid_url(url):
    """
    Validate the URL format.
    Returns True if valid, otherwise False.
    """
    url_regex = r'^(https?://)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.+)?$'
    return re.match(url_regex, url) is not None


def validate_user_input(email, url):
    """
    Validate user input for email and URL.
    Returns a dictionary with validation results.
    """
    return {
        'email': is_valid_email(email),
        'url': is_valid_url(url)
    }