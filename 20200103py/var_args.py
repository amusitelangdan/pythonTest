# -*- coding: utf-8 -*-
def power(x, n = 2):
    if not isinstance(n , int):
        raise TypeError('n must be int')
    if not isinstance(x, (int, float)):
        raise TypeError( 'x must be int or float ' )
    return x ** n
print (power(2))
# 可变参数, 计算值
def calc(numbers, n = 2):
    sum = 0
    if not isinstance(numbers, ( list, tuple)):
        raise TypeError('numbers must be list or tuple')
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError('Afferent inside value must be int or float')
        sum = sum + (number**n)
    return sum
print (calc((1,2,3,4,5)))

def calec(*numbers):
    sum = 0
    if not isinstance(numbers, ( list, tuple)):
        raise TypeError('numbers must be list or tuple')
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError('Afferent inside value must be int or float')
        sum = sum + (number**2)
    return sum
print (calec(1,2,3,4,5))
print (calec())
# 关键字参数
def person(name, age, **kv):
    print ('name', name, 'age', age, 'other', kv)
person('zhai', 30)
person('zhai', 24, city='beijing')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('jack', 24, **extra)
# 命名关键字参数
def delete(name, age, **kv):
    if 'city' in kv:
        pass
        #delattr(kv, 'city') # 删除city属性
    print ('name', name, 'age', age, 'other', kv)
delete('mary', 24, city = 'shanghai')
#def del_person(name, *, city, job):
 #   print (name, city, job)

# 允许接受一个或多个数并计算乘积
def product(x, y = 1):
    if not isinstance(x, (int, float)):
        raise TypeError('x must be int or float')
    return x*y
print (product(2, 8))
# 别人关于这个的写法：利用了可变参数
def product_other(x, *args):
    s = x
    for z in args:
        print (z)
        s = s * z
    return s
print (product_other(5))