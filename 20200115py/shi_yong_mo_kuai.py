# !/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a test module """
__author__ = 'z ru yi'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__': # 如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行。
    test()
