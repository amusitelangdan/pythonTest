# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test class limit and self"""

__author__ = 'z ru yi'


class Student(object):
    pass


s = Student()


def set_age(self, age):
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)
