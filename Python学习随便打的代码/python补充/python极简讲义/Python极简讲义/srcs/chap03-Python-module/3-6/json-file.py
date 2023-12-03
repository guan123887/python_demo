#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 15:57:09 2019

@author: yhilly
"""

import json 

#从列表中打包
data2 = [ { 'a' : 1, 'b' : 2, 
           'c' : 3, 'd' : 4, 
           'e' : 5 } ]
# 将数据保存到 JSON文件
with open('data.json', 'w') as f:
    json.dump(data2, f)

#将数据从JSON文件中读取出来
with open('data.json', 'r') as f:
    data3 = json.load(f)

print(data3[0])