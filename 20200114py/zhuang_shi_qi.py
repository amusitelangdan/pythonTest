# -*- coding: utf-8 -*-
import functools


# def log(func):
#      @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s(): ' % func.__name__)
#         return func(*args, **kw)
#
#     return wrapper

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s(): ' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('测试')
def now():
    print('2015-3-25')


f = now
f()

print(now.__name__)
# print(f.__name__)

# 设计一个decorator， 它可以作用于任何函数上，并打印该函数的执行时间
import time


def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start_time = time.time()  # 开始时间
        result = func(*args, **kw)  # 执行fnuc函数
        stop_time = time.time()  # 结束时间
        gap = stop_time - start_time  # 执行时间
        print('%s executed in %s ms' % (func.__name__, gap))
        return result

    return wrapper


@metric
def slow(x, y):
    time.sleep(0.012)
    return x + y


slow(1, 3)
