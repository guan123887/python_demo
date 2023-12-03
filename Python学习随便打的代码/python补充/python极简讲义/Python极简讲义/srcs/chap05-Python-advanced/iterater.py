# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 23:01:03 2019

@author: Yuhong
"""

my_list = [1,2,3,4]
# 创建迭代器对象
it = iter(my_list)   
 
while True:
    try:
        print (next(it))
    except StopIteration:
        print("迭代器越界啦！")
        break
print("我能正常输出！")