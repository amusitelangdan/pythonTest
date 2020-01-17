# -*- coding: utf-8 -*-
d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print (d['Michael'])
print ('abc' in d) # 监测d中是否有abc
print (d.get('abc')) # 监测d中是否有abc
print (d.pop('Bob')) # 删除d中对应的value
print (d)