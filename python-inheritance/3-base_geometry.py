#!/usr/bin/python3
"""
A module that contains an empty class
"""


class BaseGeometry:
    "An empty class"

    def __dir__(self):
        """Overrids the output of dir()"""
        return [attr for attr in super().__dir__() if attr != "__init_subclass__"]
