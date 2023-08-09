"""
A module that contains a function
"""


def is_kind_of_class(obj, a_class):
    """A function that checks the type of an object

    Args:
        obj: the object to be checked
        a_class: the class to be used

    Return:
        the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class; otherwise False.
    """
    return isinstance(obj, a_class)
