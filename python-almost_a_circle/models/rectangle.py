#!/usr/bin/python3
"""
A module that contains the Rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """
    The Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for the private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the peivate attribute width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the peivate attribute height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for the private attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for the peivate attribute x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for the private attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for the peivate attribute y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """A public method that returns the area of the rectangle"""
        return self.__width * self.__height
