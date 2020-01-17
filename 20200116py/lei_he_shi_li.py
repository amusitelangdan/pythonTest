# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test class"""

__author__ = 'z ru yi'


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


bart = Student('bart simpson', 20)
# print(bart)
bart.print_score()
