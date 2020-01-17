# -*- coding: utf-8 -*-
# 排序算法
print(sorted([5, 1, 3, 6, -21, 1000]))
# 2.按照绝对值大小排序
print(sorted([1, 5, -100, 2, 4, -300], key=abs))
# 3.字符串排序（1）区分大小写
print(sorted(['1', '2', '3', 'a', 'Z']))
# 3. 字符串排序（2）不区分大小写
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# 3. 字符串排序，不区分大小写，且进行反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


# 假设我们用一组tuple表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序, 再按成绩从高到低排序：
def by_name(t):
    return t[0].lower()


def by_score(t):
    return t[1]


print(sorted([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)], key=by_name))
print(sorted([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)], key=by_score, reverse=True))
print(list(range(1, 4)))
