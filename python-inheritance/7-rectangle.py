#!/usr/bin/python3
"""
A module that contains the class Rectangle which inherits from BaseGeometry
"""


BaseGeometry = __import__("5-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that defines a Recatngle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """Instantiation method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Defines the resturn value when str() and print() are used"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """Calculates and return the area of the rectangle"""
        return self.__height * self.__width
