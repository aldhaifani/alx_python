#!/usr/bin/python3
"""Module that defines the class Square"""


class Square:
    """
    A class that defines a square
    """

    def __init__(self, size=0) -> None:
        """Instantiation function"""
        self.size = size

    @property
    def size(self):
        """A getter method that returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """A setter method that sets the value of the size of the square"""
        if type(value) is not int:
            raise (TypeError("size must be an integer"))
        elif value < 0:
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = value

    def area(self):
        """A public method that returns the area of the square"""
        return self.__size**2
