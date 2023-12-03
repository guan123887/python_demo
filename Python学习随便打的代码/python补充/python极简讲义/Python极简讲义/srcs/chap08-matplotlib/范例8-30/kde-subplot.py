#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 12:07:51 2019

@author: yhilly
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei'] 
# 导入数据
iris = pd.read_csv("iris.csv")
iris.columns=['sepal_length','sepal_width','petal_length','petal_width','species']

#plt.figure(figsize=(16,10), dpi= 80)
#绘图
sns.kdeplot(iris.loc[iris['species'] == 'Iris-versicolor', 'sepal_length'],
             shade=False, vertical = True, color="g", label="Iris-versicolor", alpha=.7)

sns.kdeplot(iris.loc[iris['species'] == 'Iris-virginica', 'sepal_length'],
             shade=False, vertical = True, color="deeppink", label="Iris-virginica", alpha=.7)

sns.kdeplot(iris.loc[iris['species'] == 'Iris-setosa', 'sepal_length'],
             shade=False, vertical = True, color="dodgerblue", label="Iris-setosa", alpha=.7)

# Decoration
plt.title('鸢尾花花瓣长度的密度图', fontsize=16)
plt.legend()
plt.show()