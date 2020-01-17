# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test class limit and self"""

__author__ = 'z ru yi'


class Screen(object):
    __width = 0
    __height = 0

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def resolution(self):
        return self.__width * self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('width must be int or float')
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('width must be int or float')
        self.__height = value


s = Screen()
s.width = 1024
s.height = 768
print('resolution = ', s.resolution)
