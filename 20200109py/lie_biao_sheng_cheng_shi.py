# -*- coding: utf-8 -*-
import  os
# 列表生成式
# 生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (list(range(1, 11)))
# 使用循环生成list [1X1, 2x2, 3x3,...10x10]
L = []
M = []
for num in list(range(1, 11)):
    L.append(num * num)
    M.append(str(num)+'x'+str(num))
print (L)
print (M)
# 列表生成式
print ([x * x for x in list(range(1, 11))])
# for循环后面还可以加上if判断，筛选出仅偶数的平方：
print ([x * x for x in list(range(1, 11)) if x % 2 == 0])
# 还可以使用两层循环，可以生成全排列：
print ([m + n for m in 'XYZ' for n in 'ABC'])
# 列出当前目录下的所有文件和目录名
print ([d for d in os.listdir('.')]) # os.listdir 可以列出文件和目录
# 列表生成事使用两个变量生成list
a = { 'x': 'A', 'y': 'B', 'z': 'C' }
print ([k + '=' + v for k, v in a.items()])
# 把一个额list中所有的字符串变成小写
s = ['Hello', 'World']
print ([i.lower() for i in s])
# 练习： 如果list中既包含字符串，又包含整数，请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
def format(list):
    if len(list) == 0:
        print ('数组为空')
        return
    arr = list
    print ([ item.lower() if isinstance(item, str) else item for item in arr])
format(['Hellow', 12, 'World'])
format([])