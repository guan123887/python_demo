#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 19:02:48 2019

@author: yhilly
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#方案1：利用pandas读取数据
#sns.set(style = "ticks")
#iris = pd.read_csv('iris.csv', header = None)
#
#iris.columns=['sepal_length','sepal_width','petal_length','petal_width','species']
#
#sns.boxplot(x = iris['sepal_length'], data = iris)
#plt.show()

# 方案2：用Seaborn导入数据
df = sns.load_dataset('iris')
 
# 绘制一维箱体图
sns.boxplot( x = df["sepal_length"] )
#plt.show()

