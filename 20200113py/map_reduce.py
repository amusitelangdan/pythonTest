# -*- coding: utf-8 -*-
from functools import reduce


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
#print(list(r))
# 用reduce 实现序列求和


def add(x, y):
    if isinstance(x, (int, float)) == False:
        print('第一个值格式错误')
        return
    if isinstance(y, (int, float)) == False:
        print ('第二个值格式错误')
        return
    #print (x + y)
    return x + y
reduce(add, [1,2,3,4,5])

# 把str转换为int的函数
def fn(x, y):
    return x * 10 + y;
def char2num(s):
    d = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }
    return d[s]
reduce(fn, map(char2num, '13579'))
#print (reduce(fn, map(char2num, '13579')))

# 整理成一个str => int 的函数
DIGITS = { '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9 }
def str2int(s):
    def fn(x, y):
        return x * 10 + y;
    def char2num(x):
        return DIGITS[x]
    return reduce(fn, map(char2num, s))

#print('234556')

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normal(lists):
    def char(s):
        return s.title()
    return list(map(char, lists))
print(normal(['adam', 'LISA', 'barT']))

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(s):
    def ride (x, y):
        return x * y
    return reduce(ride, s)
print(prod([1,2,3,4]))

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    def fn(x, y):
        return x * 10 + y
    arr = s.split('.')
    def char2float(item):
        return int(item)
    if len(arr) == 2:
      return reduce(fn, map(char2float, arr[0])) + reduce(fn, map(char2float, arr[1])) / 10 ** len(arr[1])
    elif len(arr) == 1:
        return reduce(fn, map(char2float, arr))
print(str2float('12.13'))
print(str2float('12'))

