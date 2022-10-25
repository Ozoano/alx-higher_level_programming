#!/usr/bin/python3
"""contains a rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents a rectangle"""
    def __init__(self, width, height):
        """inst ntiation of a rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
