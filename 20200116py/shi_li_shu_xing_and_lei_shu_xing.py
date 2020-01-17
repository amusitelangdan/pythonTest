# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test class limit and self"""

__author__ = 'z ru yi'


class Student(object):
    __count = 0

    def __init__(self, name):
        if name:
            Student.__count += 1
            print(self.__count)
        else:
            print('输入name')

    def get_count(self):
        return self.__count


a = Student('1')
b = Student('2')
c = Student('3')
# print(Student().get_count)
