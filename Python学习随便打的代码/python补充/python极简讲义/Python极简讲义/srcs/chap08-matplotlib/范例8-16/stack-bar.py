#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:47:09 2019

@author: yhilly
"""

#叠加
import numpy as np
import matplotlib.pyplot as plt
#设置字体以便支持中文
plt.rcParams['font.sans-serif']=['SimHei']

# 用于绘制图形的数据
n_groups = 4
means_frank = (90, 55, 40, 65)
means_guido = (85, 62, 54, 20)

# 创建图形
fig, ax = plt.subplots()

#定义条形图在横坐标上的分类位置
index = np.arange(n_groups)

bar_width = 0.35
opacity = 0.8
#画第一个条形图
rects1 = plt.bar(index,      #定义第一个条形图的X坐标信息
                 means_frank, #定义第一个条形图的Y轴信息
                 bar_width,   #定义条形图的宽度
                 alpha = opacity,    #定义图形透明度
                 color="w",edgecolor="k",
                 hatch='.....',
                 label = '张三')    #定义第一个条形图的标签信息
#画第二个条形图
rects2 = plt.bar(index, # 与第一个条形图在X周上无缝“肩并肩”
                means_guido, 
                 bar_width,
                 bottom = means_frank,
                alpha = opacity,
                 color="w",edgecolor="k",
                 hatch=r'\\\\',
                label = '李四') #定义第二个条形图的标签信息

plt.xlabel('课程')
plt.ylabel('分数')
plt.title('分数对比图')
plt.xticks(index, ('A', 'B', 'C', 'D'))
plt.legend()
plt.show()