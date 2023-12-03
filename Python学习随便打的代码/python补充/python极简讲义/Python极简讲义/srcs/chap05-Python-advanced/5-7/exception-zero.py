# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:29:50 2019

@author: Yuhong
"""

def this_fails():
    x = 1 / 0
try:
    this_fails()
except ZeroDivisionError as err:
     print('运行时异常:', err)
finally:
    print("我是来演示的，非必需！")
print("我是正常代码！")