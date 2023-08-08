#!/usr/bin/python3
"""Module that defines the class Square"""


class Square:
    """
    A class that defines a square
    """

    __size = 0

    def __init__(self, size) -> None:
        """Instantiation function"""
        self.__size = size
