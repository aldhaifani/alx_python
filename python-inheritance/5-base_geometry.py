#!/usr/bin/python3
"""
A module that contains the class BaseGeometry
"""


class BaseGeometryMetaClass(type):
    """
    The meta class of BaseGeometry
    """

    def __dir__(cls) -> None:
        """Overrids the output of dir()"""
        return [attr for attr in super().__dir__() if attr != "__init_subclass__"]


class BaseGeometry(metaclass=BaseGeometryMetaClass):
    "An empty class"

    def __dir__(cls) -> None:
        """Overrids the output of dir()"""
        return [attr for attr in super().__dir__() if attr != "__init_subclass__"]

    def area(self):
        """Defines a public instance method area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates the parameter value
        Assumes that the parameter name is always a string
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
