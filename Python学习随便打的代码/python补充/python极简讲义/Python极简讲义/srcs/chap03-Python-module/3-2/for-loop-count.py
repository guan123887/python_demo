#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:46:36 2019

@author: yhilly
"""

#统计词频
colors = ['red', 'blue', 'red', 'green', 'blue', 'yellow']
result = {}
for color in colors:
    if result.get(color)==None:
        result[color] = 1
    else:
        result[color] += 1
print (result)
