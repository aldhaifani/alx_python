#!/usr/bin/python3
"""
A module that contains an empty class
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
