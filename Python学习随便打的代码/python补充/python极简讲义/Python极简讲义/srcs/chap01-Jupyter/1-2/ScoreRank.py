# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 10:54:09 2018

@author: Yuhong
"""

#这是一个演示while循环的范例
while True:
    score = int(input("请输入你的成绩 : "))
    if 90 <= score <= 100:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print("D")
    else:
        print('''你的分数有点低！''')
