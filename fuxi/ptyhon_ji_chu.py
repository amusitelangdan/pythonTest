# -*- coding: utf-8 -*-
# 数据类型：整数 int、 浮点数 float、字符串 str、布尔值 True False 【与或非：and or not】、空值 None、 变量
# 常量 ： 不能变的量，通常是用大写的变量名表示常量
# 两种除法：
#        1. / ： / 除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
#        2. // ： 成为地板除，两个整数的除法仍然是整数，即使除不尽（只取结果的整数部分）
#        3. % ： 两个整数相除的余数
#        注意⚠️：无论整数做//除法还是取余数，结果永远是整数，所以整数运算结果永远是精确的


# 字符编码
# Unicode 编码
# ord()函数获取字符的整数表示，chr()函数把编码转换为相应的字符
# unicode 表示的str 通过 encode() 方法可以编码为指定的bytes
# 'ABC'.encode('ascii')
# 反之，读到的bytes想要转为str就需要decode()方法： 当bytes中包含无法解码的字节，decode() 方法会报错此时可以传入errors = 'ignore'忽略错误的字节
# b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
# len()函数计算str的字符书，如果换成bytes，len()函数就计算字节数
# 1个中文字符经过utf-8编码后通常会占用3个字节，而一个英文字符只占用1个字节
# 为防止乱码问题，我们应当坚持使用utf-8编码对str和bytes进行转换
# 由于python的源代码是一个文本文件，所以代码中出现中文的时候，在保存源代码的时候就必须指定保存为utf-8编码，通常在文件开通写上这两行
# ### !/usr/bin/env python 3  ####
# ### -*- coding: utf-8 -*- ###
# 第一行是为了告诉Linux/OS X系统，这是一个python可执行程序，Windows会忽略这个注释
# 第二行注释是为了告诉python解释器，暗战utf-8编码进行读取源代码
# 格式化：
# 如何输出格式化的字符串？    例如： 亲爱的xxx你好！您xx月的话费是xx，余额是xx之类，xx表示根据变量改变
# python中，采用的格式化方式和c语言一样，都是使用 % 实现：
# 'hello， %s' % 'world'  -> 输出为 'hello, world'
# 'Hi, %s, you have $%d.' % ('Michael', 10000) -> 输出为: 'Hi, Michael, you have $1000000.'
# 注意⚠️：
# % 运算符用来格式化字符串
# %s表示字符串替换（如果不确定应该用什么。%s会把任何数据类型转换为字符串）、 %d表示整数替换、 %f表示浮点数替换、%x表示十六进制替换，有几个%？占位符，后面就要跟几个变量或者值，顺序要对应好，如果只有一个%？，括号可以省略


# list： 列表
# 列表就是一种有序的集合，可以随时添加删除其中的元素，也就是其他语言中的数组
# len()函数可以获得list的个数
# 使用-1做索引，可以直接获取最后一个元素
# 添加数据（追加）： append('aaa')
# 添加数据（指定位置）： insert(1, 'jack')
# 删除数据（末尾的数据）： pop()
# 删除数据（指定位置）： pop(1)


# tuple: 元组
# tuple 元组一旦初始化就不能修改
# tuple 没有append() insert() 方法，其他获取元素的方法和list是一样的
# tuple陷阱： 当定义一个tuple的时候，tuple的元素就必须被确定下来
# 定义一个空的tuple时写成() t = ()
# 定义一个元素的tuple时 t = (1,)


# 条件判断：
# if


# 循环
# for循环 for n in range(1, 10)
# while循环 只要条件满足。就不断循环，条件不满足时退出循环
# break可以提前退出循环
# continue 跳过档次循环，直接开始下一次循环


# dict
# dict：字典全称dictionary，在其他语言中成为map，使用键 - 值（key-value）存储，具有极快的查找速度
# 判断key不存在：
# 1.in判断key是否存在： 'T' in d 返回布尔值
# 2.通过dict提供的get() 方法，如果key不存在，可以返回None，或者自己指定的value
# d.get('T')   d.gey('T', -1)
# 注意⚠️：
# 返回None的时候python的交互环境下不显示结果
# 要删除一个key，使用pop(key)，对用的value也会删除


# set
# set和dict蕾丝，也是一组key的集合，但不存储value，由于key不能重复，所以在 set中没有重复的key。
# s = set([1, 2, 3]) 输出{1, 2, 3}
# 重复元素在set中自动被过滤
# 通过add(key)方法可以添加元素的set中，可以重复添加，但不会有效果
# 通过remove(key)方法可以删除元素
# 注意⚠️：
# set和dict唯一的区别在于没有存储对应的value，但是，set的原理和dict一样
