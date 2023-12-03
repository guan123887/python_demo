# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 23:07:38 2019

@author: Yuhong
"""

def avg(score):
#    assert len(score) != 0
    assert len(score) != 0,  "列表为空，咋整啊！"
    return sum(score) / len(score)

score = []
print("平均分数为:",avg(score))