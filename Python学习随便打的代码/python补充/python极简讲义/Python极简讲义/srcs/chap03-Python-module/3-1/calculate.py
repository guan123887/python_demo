# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 07:23:10 2018

@author: Yuhong
"""
 # 我所在的文件是calcalute.py
 
from parameters import PI

def calc_round_area(radius):                    #定义圆形面积求解函数
    return PI * (radius ** 2)

def run():
    print ("圆形面积为: ", calc_round_area( 5 )) #调用圆形面积求解函数

run()