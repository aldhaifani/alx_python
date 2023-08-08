#!/usr/bin/python3
"""Module that defines the class Square"""


class Square:
    """
    A class that defines a square
    """

    __size = 0

    def __init__(self, size=0) -> None:
        """Instantiation function"""
        if type(size) is not int:
            raise (TypeError("size must be an integer"))
        elif size < 0:
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size

    def area(self):
        """A public method that returns the area of the square"""
        return self.__size**2
