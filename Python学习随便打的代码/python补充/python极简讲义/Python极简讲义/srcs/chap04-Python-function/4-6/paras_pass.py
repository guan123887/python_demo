# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 17:36:05 2019

@author: Yuhong
"""


def numFunc(x):
    print('在函数中，形参x的地址为：', id(x))
    print('在函数中，形参x的值为：', x)
    x = x + 1
    print('在函数中，x的更新值为：', x)
    print('在函数中，x的地址更新为：',id(x))

a = 3
print('在函数外，实参a的地址为：',id(a))
numFunc(a)
print('在调用函数之后，实参a的值为：',a)
