#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2020.01.02
@author : Bert
'''
import os
import random


# PersonNum = int(input("请输入剪子（0） 石头（1） 包袱（2）:"))
# PcNum = int(random.randint(0,2))
# print(PcNum)
#
# if (PersonNum == 0 and PcNum == 1) or  (PersonNum == 1 and PcNum == 2) or (PersonNum == 2 and PcNum == 0):
#     print("输了，再来一局，决战到天亮！")
#
# elif (PersonNum == 0 and PcNum == 2) or  (PersonNum == 1 and PcNum == 0) or (PersonNum == 2 and PcNum == 1):
#     print("获胜，你厉害")
# else:
#     print("哈哈，平局，再来一局")

# num = 0
# i = 1
# while i <= 100:
#     num = num + i
#     i+=1
# print("1-100的累计之和为:%d"%num)

sum = 0
i = 1
while i <= 100:
    if i%5 == 0:
        sum +=i
        print("%d 能被5整除"%i)
    else:
        print("%d 不能被整除"%i)
    i+=1
print("1-100之间能被5整除的数之和为：%d"%sum)