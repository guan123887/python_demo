# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 14:57:58 2019

@author: Yuhong
"""

# 计算面积函数
def area(width, height):
    '''
    功能：计算矩形的面积

    参数：
    ----------
    width : 数值型
        矩形的宽度
    height :数值型
        矩形的高度

    返回值
    -------
    rec_area: 数值型
        矩形的面积：width * height
    '''
    rec_area = width * height
    return rec_area

w = 4
h = 5
print("width = ", w, " height =", h, " area = ", area(w, h))
