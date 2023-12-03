# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 12:01:54 2019

@author: Yuhong
"""

def some_kwargs(name, age, sex):
    print("姓名:", name)
    print("年龄:", age)
    print("性别:", sex)

kwargs_dic = {'name' : 'Alice', 'age' : 10, 'sex' : '女'}

some_kwargs(**kwargs_dic)