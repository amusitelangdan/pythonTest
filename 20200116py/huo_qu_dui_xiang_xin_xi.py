# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test class limit"""

__author__ = 'z ru yi'

print(type(123))
print(type('str'))
print(type(abs))
a = type(123) == type(456)
b = type(1213) == int
c = type('abc') == str
d = type('abc') == type(123)
print(a, b, c, d)

import types


def fn():
    pass


e = type(fn) == types.FunctionType
f = type(abs) == types.BuiltinFunctionType
print(e, f)


class Animal(object):
    pass


class Dog(Animal):
    pass


class Husky(Dog):
    pass


g = Animal()
h = Dog()
i = Husky()

print(isinstance(i, Husky))
print(isinstance(i, Dog))
print(isinstance(i, Animal))
