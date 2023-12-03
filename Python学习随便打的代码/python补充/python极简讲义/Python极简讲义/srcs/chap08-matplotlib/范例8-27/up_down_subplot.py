#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 16:58:32 2019

@author: yhilly
"""

import seaborn as sns, matplotlib.pyplot as plt
#导入数据集合
df = sns.load_dataset("iris")

fig,axes=plt.subplots(2,1) #2行1列共两个子图

sns.boxplot(x = "species",y = "petal_width",data = df, orient="v", ax = axes[0]) #上子图垂直显示

sns.boxplot(y = "species",x = "petal_length",data = df, orient="h", palette="Set2", ax = axes[1]) #下子图水平显示