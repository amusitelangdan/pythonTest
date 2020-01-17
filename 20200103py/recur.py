# -*- coding: utf-8 -*-
# 递归函数
def fact(n):
    if n == 1:
        return 1
    return  n * fact(n - 1)

print (fact(3))
#fact(10000)
# 尾递归优化, python并没有作出优化
def fact_other(n):
    return fact_iter(n, 1)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num -1, num * product)
fact_other(100)

# 汉诺塔的移动可以用递归函数非常简单地实现。
# 请编写move(n, a,b, c)函数，它接收参数n，表示3哥柱子A，B， C中的一个柱子A的数量，然后打印出把所有盘子从A借助B移动到C的方法
# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
# move(3, 'A', 'B', 'C')
# 这个意思是，当A上面有三个盘子，首先第一次将a上面的一个盘子移动到c，此时a只有两个盘子，将a中一哥盘子移动到b，a上面此时只有一个，将c上面的盘子移动到b，此时b有两个盘子，c没有盘子
# 此时总结一下，a有一个盘子， b有两个盘子，c没有盘子
# 然后将a的盘子移动到c，此时a没有盘子，b两个盘子，c有一个盘子
# 将b的一个盘子给a，一个盘子给c 此时a有一个盘子，c有两个盘子
# 将a的盘子给c，此时c有三个盘子，a没有盘子，b也没有盘子
def move(n , a, b, c):
    if n == 1:
        print (a, '--->', c)
    else:
        move(n-1, a, c, b)
        print (a, '--->', c)
        move(n - 1, b, a, c)
move(10, 'A', 'B', 'C')