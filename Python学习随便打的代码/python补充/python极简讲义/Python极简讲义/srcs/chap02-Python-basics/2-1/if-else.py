# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 14:27:07 2018

@author: Yuhong
"""


score = 89
#if score >= 90 and score <= 100:    # 判断值是否在0~10之间
if 90 <= score <= 100:    
    print ('A')
elif score >= 80 and score <= 89: 
    print('B')
# 输出结果: hello
 
num = 10
if num < 0 or num > 20:    # 判断值是否在小于0或大于20
    print ('valid')
else:
    print ('invalid')
# 输出结果: invalid
 
num = 7
# 判断值是否在0~5或者10~20之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 20):    
    print ('valid')
else:
    print ('invalid')
# 输出结果: invalid

a_dict = {}  #这是一个空字典
if not a_dict: 
    print("这是一个空字典！")
