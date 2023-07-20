#!/usr/bin/python3
def is_digit_in_string(string):
    """
    Checks if there is a digit in a string.

    Args:
      string: The string to check.

    Returns:
      True if there is a digit in the string, False otherwise.
    """

    for c in string:
        if c.isdigit():
            return True
    return False


def is_upper_in_string(string):
    """
    Checks if there is atleast one uppercase character in a string.

    Args:
      string: The string to check.

    Returns:
      True if there is atleast one uppercase character in the string,
      False otherwise.
    """

    for c in string:
        if c.isupper():
            return True
    return False


def is_lower_in_string(string):
    """
    Checks if there is atleast one lowercase character in a string.

    Args:
      string: The string to check.

    Returns:
      True if there is atleast one lowercase character in the string,
      False otherwise.
    """

    for c in string:
        if c.islower():
            return True
    return False


def validate_password(password):
    """
    Validates a password according to the following:
    1. The password should be at least 8 characters long.
    2. The password should contain at least one uppercase letter,
    one lowercase letter, and one digit.
    3. The password should not contain spaces.

    Args:
      password: The password to be validated

    Returns:
      True if the password passes all the checks, and False otherwise.
    """
    return (
        is_digit_in_string(password)
        and is_lower_in_string(password)
        and is_upper_in_string(password)
        and (" " not in password)
    )
