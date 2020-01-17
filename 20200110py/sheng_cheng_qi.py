# -*- coding: utf-8 -*-
L = [ x * x for x in range(10) ]
G = ( x * x for x in range(10) )
#print (L)
#print (G)
#print (next(G))
#print (next(G))
#print (next(G))
g = ( x * x for x in range(10) )
#for n in g:
#    print (n)s
# 输出斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield(b)
        a, b = b, a + b
        n += 1
    return 'done'
fib(6)
print (fib(6))
# 杨辉三角定义如下：
#          1
#         / \
#        1   1
#       / \ / \
#      1   2   1
#     / \ / \ / \
#    1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1

# 把每一行看做一个list，试写一个generator，不断输出下一行的list：

def triangles(n):
    L = [1]
    yield(L)
    while n:
        L = [1]+[L[n]+L[n+1] for n in range(len(L)-1)] + [1]
        yield(L)
print (triangles(5))
gx = (x for x in triangles(6))
for x in gx:
    print(x)
