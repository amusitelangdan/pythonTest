# -*- coding: utf-8 -*-
# 迭代：即循环遍历
# 1. for 循环使用在dict上
a = {'a': 1, 'b': 2, 'c': 3}
for item in a:
    print (item)
for value in a.values():
    print (value)
for k, v in a.items():
    print (k, v)
# 2. 迭代字符串
for value in 'AbcDEFgh':
    print (value)
# 3.如何判断一个对象是可迭代对象？----通过collection模块的iterable类型来判断：
# 最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, v in enumerate(['a', 'b', 'c']):
    print (i, v)

# 练习：请使用迭代查找一个list中最小和最大的值，并返回一个tuple：
def lookup(list):
    arr = list
    if len(arr) == 0:
        return (None, None)
    else:
        min = arr[0]
        max = arr[1]
        for item in arr:
            if item > max:
                max = item
            if item < min:
                min = item
        return (max, min)
print (lookup([1, 3, 0, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
