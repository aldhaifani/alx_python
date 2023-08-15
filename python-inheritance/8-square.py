#!/usr/bin/python3
"""
A module that contains the class Sqaure which inherits from Rectangle
"""

Rectangle = __import__("7-rectangle").Rectangle


class Square(Rectangle):
    """
    A class that defines a Square that inherits from a Rectangle
    """

    def __init__(self, size):
        """Instantiation method"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
