#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:38:10 2019

@author: yhilly
"""

import matplotlib.pyplot as plt
import numpy as np

#0到4区间，以间隔0.2被均匀分割
data = np.arange(0, 4, 0.2)

# 分别使用红色的点划线、蓝色的方块和绿色的三角形来区分这3条曲线
plt.plot(data, data, 'r-.', data, data**2, 'bs', data, data**3, 'g^')

plt.show()

plt.savefig('mult_lines.png',dpi=600)

#输出为eps格式
#plt.savefig('mult_lines.eps',dpi=600)