#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 21:44:08 2019

@author: yhilly
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 导入数据
iris = pd.read_csv("iris.csv")
iris.columns=['sepal_length','sepal_width','petal_length','petal_width','species']
# 绘图
plt.figure(dpi = 200)
#sns.violinplot(x='species', y = 'sepal_length', data = iris, scale='width', inner='quartile')

sns.violinplot(x='species', y = 'sepal_length', data = iris, split = True, scale='width', inner="box")

# 输出显示
plt.title('Violin Plot', fontsize=10)
plt.show()

