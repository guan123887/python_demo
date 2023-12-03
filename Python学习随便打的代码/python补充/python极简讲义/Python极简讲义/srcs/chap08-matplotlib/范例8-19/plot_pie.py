#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 19:14:48 2019

@author: yhilly
"""


import matplotlib.pyplot as plt
# 为在Matplotlib中显示中文，设置特殊字体
plt.rcParams['font.sans-serif']=['SimHei']
#为图片设置大小和分辨率
plt.figure(figsize = (9, 6), dpi = 100)
x = [217,743,426]
labels = ['走路去','自行车','公交车']
explode = [0,0.05,0]

_, _, autotexts = plt.pie(x = x,labels = labels,shadow = 1,
                          autopct = '%.1f%%',explode = explode)
#将饼状图中的字体改成白色
for autotext in autotexts:
    autotext.set_color('white')

plt.title('3种去学校的方式')
plt.show()

