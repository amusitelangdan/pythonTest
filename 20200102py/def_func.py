# -*- coding: utf-8 -*-
import math
def my_abs(x):
    if not isinstance(x ,(int, float)):
        raise TypeError('类型错误')
    if x > 0:
        return x
    else:
        return -x;
# print (my_abs(-100))
# print (my_abs('-a'))
# print (my_abs('-a'))
# math.sqrt() 求平方根
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0ax
# 2
#  +bx+c=0 的两个解。
def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('a的类型不符合要求')
    if not isinstance(b, (int, float)):
        raise TypeError('b的类型不符合要求')
    if not isinstance(c, (int, float)):
        raise TypeError('c的类型不符合要求')
    root = (b ** 2) - (4 * ( a * c ))
    if root < 0:
        raise TypeError('b的值需要满足b^2-4ac>0')

    sum = math.sqrt(root)
    nx = (-b + sum) / (2 * a)
    ny = (-b - sum) / (2 * a)
    return nx, ny
x, y = quadratic(2, 6, 4)
print (x, y)