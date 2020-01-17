# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test class limit"""

__author__ = 'z ru yi'


class Student(object):
    def __init__(self, name, gender):
        if gender != '男' and gender != '女':
            print('性别输入应为男或者女')
            return
        else:
            self.__name = name
            self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender != '男' and gender != '女':
            print('性别输入应为：男或者女')
            return ValueError('性别输入应为：男或者女')
        else:
            self.__gender = gender


dart = Student('jack', '女')
# print(dart.get_gender())
dart.set_gender('男')
