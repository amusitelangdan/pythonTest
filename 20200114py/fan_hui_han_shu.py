# -*- coding: utf-8 -*-
def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


# 利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
    f = [0]

    def counter():
        f[0] += 1
        return f[0]

    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(),counterA())
