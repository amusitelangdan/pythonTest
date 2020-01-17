# -*- coding: utf-8 -*-
# 在一个list中，删掉偶数，只保留奇数
def is_add(item):
    return item % 2 == 1
print(list(filter(is_add, [1,2,3,4,5,6,7,8,9,10])))
# 删除序列中的空字符串
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['','1','3','4'])))
# 计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
#
# 首先，列出从2开始的所有自然数，构造一个序列：
#
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#
# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
#
# 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
#
# 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
#
# 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#
# 不断筛下去，就可以得到所有的素数。
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x: x % n > 0
def primes():
    yield 2
    it = _odd_iter() # 出初始化序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) #构造新序列
# 打印1000以内的素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    # 转成字符串，反转过来对比原字符串看返回true / false
    s = str(n)
    return s == s[::-1]
print(list(filter(is_palindrome,range(1000))))