#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 09:24:30 2019

@author: yhilly
"""

import numpy as np
import matplotlib.pyplot as plt

objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]

#修改：填充色为黑色，融合标签标签在参数中
plt.barh(y_pos, performance, align='center', alpha = 0.5, color = 'k', 
        tick_label = objects)
#修改X轴的标题
plt.xlabel('用户量')
plt.title('数据分析程序语言使用分布情况')

plt.show()