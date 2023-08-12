"""
A module that contains a function
"""


def inherits_from(obj, a_class):
    """A function that checks the type of an object

    Args:
        obj: the object to be checked
        a_class: the class to be used

    Return:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class ; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
