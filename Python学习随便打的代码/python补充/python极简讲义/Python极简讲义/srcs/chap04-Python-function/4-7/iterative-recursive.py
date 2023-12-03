# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 20:57:00 2019

@author: Yuhong
"""


#用递推的方式计算阶乘
def iterative_fact( n ):  
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
  
# 递归方式计算阶乘
def recursive_fact( n ):
    if n <= 1 :
        return n;
    return n * recursive_fact(n - 1)
	
#调用非递归方法计算
num = 5
result = iterative_fact( num );
print("递推方法：{}!= {}".format(num, result))
#调用递归方法计算
result = recursive_fact(num)
print("递归方法：{}!= {}".format(num, result))