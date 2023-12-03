# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:35:09 2019

@author: Yuhong
"""

def mySum(*args): 
    sum = 0
    for i in range(0, len(args)): 
        sum = sum + args[i] 
    return sum 
  
# 可变参数函数调用 
print(mySum(1, 2, 3, 4, 5)) 
print(mySum(20.1, 30.2)) 