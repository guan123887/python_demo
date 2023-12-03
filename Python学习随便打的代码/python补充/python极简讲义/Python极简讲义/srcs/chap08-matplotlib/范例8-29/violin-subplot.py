#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 22:38:30 2019

@author: yhilly
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 导入数据
iris = pd.read_csv("iris.csv")
iris.columns=['sepal_length','sepal_width','petal_length','petal_width','species']

# 绘图设置
fig, axes = plt.subplots(2, 2, figsize=(7, 5), sharex=True)

sns.violinplot(x = 'species', y = 'sepal_length', 
               data = iris, split = True, 
               scale='width', inner="box", 
               ax = axes[0, 0])
sns.violinplot(x = 'species', y = 'sepal_width', 
               data = iris, split = True, scale='width', 
               inner="box", 
               ax = axes[0, 1])
sns.violinplot(x = 'species', y = 'petal_length', 
               data = iris, split = True, scale='width', 
               inner="box", 
               ax = axes[1, 0])
sns.violinplot(x = 'species', 
               y = 'petal_width', 
               data = iris, split = True, 
               scale='width', inner="box", 
               ax = axes[1, 1])
# 输出显示
plt.setp(axes, yticks=[])
plt.tight_layout()
