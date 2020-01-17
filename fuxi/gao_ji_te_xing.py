# -*- coding: utf-8 -*-
# 切片 splice
# 例子： L是一个list  L[0:3]表示，从索引0开始，知道索引3为止，但不包括索引3， 如果第一个索引是0，还可以省略 L[:3]
# 倒数切片： L[-10:]表示后10个数
# 注意⚠️： tuple也可以用切片操作，只是操作的结果仍是tuple
# 注意⚠️：字符串也可以使用切片操作，只是结果仍是str


# 迭代
# 也就是循环遍历， 定义： 如果给定一个list或tuple，我们可以通过for循环来遍历这个list 或者tuple，这种遍历我们成为迭代(iteration)
# for...in...:
# 注意⚠️： 默认情况下，dict迭代的是key，如果要迭代value，可以使用 for value in d.value()   同时迭代key和value： for k, v in d.items()
# ⚠️：字符串也可以迭代
# 判断对象是否可迭代：
# form collections import Iterable
# isinstance('abc', Iterable) # 判断是否可迭代
# 注意⚠️： 如果想要下标怎么办？ python内置的 enumerate可以把一个list变成索引-元素对，这就可以在for循环中同时迭代索引和元素本身
# for i, value in enumerate(list)

def search_max_min(list1):
    max1 = list1[0]
    min1 = list1[0]
    if len(list1) == 0:
        print('数组为空')
        return
    if len(list1) == 1:
        max1 = list1[0]
        min1 = list[0]
    for item in list1:
        if not isinstance(item, (int, float)):
            raise ValueError('list is item must be int or float')
        if max1 < item:
            max1 = item
        if min1 >= item:
            min1 = item
    return max1, min1


print(search_max_min([1, 2, 3, 4, 5, 6, 7]))

# 列表生成式
# [x*x for x in range(1,11)]
# [x * x for x in range(1, 11) if x % 2 == 0]
# [m + n for m in 'ABC' for n in 'XYZ']
# [ item.lower() if isinstance(item, str) else item for item in arr]


# 生成器
# 下次总结
