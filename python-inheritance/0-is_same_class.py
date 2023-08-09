"""
A module that contains a function
"""


def is_same_class(obj, a_class):
    """A function that checks the type of an object

    Args:
        obj: the object to be checked
        a_class: the class to be used

    Return:
        True if obj is exactly an instance of a_class
    """
    return isinstance(obj, a_class) and type(obj) == a_class
