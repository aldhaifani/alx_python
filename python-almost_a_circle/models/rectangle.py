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
        self.__width = value

    @property
    def heigth(self):
        """Getter method for the private attribute heigth"""
        return self.__heigth

    @heigth.setter
    def heigth(self, value):
        """Setter method for the peivate attribute heigth"""
        self.__heigth = value

    @property
    def x(self):
        """Getter method for the private attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for the peivate attribute x"""
        self.__x = value

    @property
    def y(self):
        """Getter method for the private attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for the peivate attribute y"""
        self.__y = value
