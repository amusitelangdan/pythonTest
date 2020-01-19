# -*- coding: utf-8 -*-

# 高阶函数
# map/reduce
# map() 接收两个参数， 一个是函数， 一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterable返回
# def f(x):
#    return x * x
# fx = map(f, range(1, 10))
# ⚠️： map()传入的第一个参数是f，即函数对象本身，由于结果是一个Iterator， Iterator， 因此通过list() 函数让他把整个序列都计算出来并返回一个list
# reduce把一个函数作用在一个序列 [x1,x2,x3...]上，这个函数必须接收两个参数， reduce把结果继续和序列的下一个元素做累积计算，和map可以搭配
# from functools import reduce
# def add(x, y):
#       return x + y
# reduce(add, [1, 2,3,4])

# filter
# filter用于过滤序列，与map() 相似，接收一个函数一个序列， 不同的是， filter把传入的函数一次作用一每个元素，然后根据返回值 True还是False决定保存还是丢弃该元素
# def is_odd(n):
#     return n % 2 == 1
#
# list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]

# sorted
# 排序算法
# 它可以接收一个key来实现自定义排序
# sorted([36, 5, -12, 9, -21], key=abs) # 绝对值大小排序
# 默认从小到大， 要进行反向排序， 不必改动key函数，可以传入翟三个参数reverse = True
# sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。


# 返回函数
# 函数作为返回值
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
#
# f = lazy_sum(1, 3, 5, 7, 9)
# f
# <function lazy_sum.<locals>.sum at 0x101c6ed90>
# 调用函数f时，才真正计算求和的结果：
#
# f()
# 25

# 闭包
# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs

# def createCounter():
#     f = [0]
#     def fn(j):
#         f[0] += 1
#         return f[0]
#     return fn
# counterA = createCounter()
# print(counterA(), counterA(), counterA(),counterA())


# 匿名函数
# lambda
# lambda x : x * x 实际上是：
# def f(x):
#    return x * x
# 关键字lambda表示匿名，冒号前面的x表示函数参数， 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果


# 装饰器
# 在代码运行期间动态增加功能的方式，成为"装饰器"

