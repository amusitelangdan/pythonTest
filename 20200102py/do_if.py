# -*- coding: utf-8 -*-
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
# 小明身高1.75，体重80.5kg。根据BMI公式（体重除以身高的平方）帮小明酸楚他的BMI指数，并根据BMI指数：
# 1 低于18.5：过轻
# 2 18.5-25：正常
# 3 25-28：过重
# 4 28-32：肥胖
# 5 高于32：严重肥胖
bmi = (80.5 * 80.5) / 175
if bmi <= 18.5:
    print ('过轻')
elif bmi > 18.5 and bmi <= 25:
    print ('正常')
elif bmi > 25 and bmi <= 28:
    print ('过重')
elif bmi > 28 and bmi <= 32:
    print ('肥胖')
elif bmi > 32:
    print ('严重肥胖')
else:
    print('bmi出现bug')