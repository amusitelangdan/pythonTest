# -*- coding: utf-8 -*-
# 调用函数
# python 内置了很多游泳的函数，我们可以直接调用

# 普通函数
# #print()函数
# #input()函数


# 进制转换函数
# #1.bin(), oct(), hex() 进制转换函数（带前缀）
# ## 十进制转换为二进制 bin()
# ## 十进制转换为八进制 oct()
# ## 十进制转换为十六进制 hex()

# #2.'{0:b/o/x}'.format()进制转换函数（不带前缀）
# ## 十进制转换为二进制 '{0:b}'.format(int)
# ## 十进制转换为八进制 '{0:o}'.format(int)
# ## 十进制转换为十六进制 '{0:x}'.format(int)
# 注意⚠️ hex函数比格式化字符串函数format满，不推荐使用

# #3. int(’’,2/8/16)转化为十进制函数（不带前缀）
# ## 二进制转为十进制 int('1010',2)
# ## 八进制转为十进制 int('014', 8)
# ## 十六进制转十进制 int('0xc',16)

# #4. '{0:d}'.format() 进制转换为十进制函数
# ## 二进制转十进制 '{0:d}'.format(0b11)
# ## 八进制转十进制 '{0:d}'.format(0o14)
# ## 十六进制转十进制 '{0:d}'.format(0x1f)

# #5. eval() 进制转换为十进制函数： eval比int慢，不推荐使用


# 求数据类型函数
# #1. type()
# #2. isinstance(): 推荐使用费 功能： 判断变量是否属于某一数据类型，可以判断子类是否属于父类


# 关键字函数
# #1. keyword.kwlist() 函数： 查看关键字 import keyword
# 写不动了，详情： https://blog.csdn.net/lm_is_dc/article/details/80048400



# 定义函数
# 使用def定义函数
# 空函数： def: nop(): pass
# 参数检查
# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x



# 函数的参数
# 位置参数：js里面的形参
# 关键字参数 **kw
# 命名关键字参数： 使用*进行分割，后面的参数被视为命名关键字参数
# 参数组合：
# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)



# 递归函数
# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数
# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)
