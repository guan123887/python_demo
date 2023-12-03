#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 11:00:14 2019

@author: yhilly
"""

import seaborn as sns, matplotlib.pyplot as plt
#导入数据集合
df = sns.load_dataset("iris")

fig,axes=plt.subplots(1,2,sharey = True) #一行两列共两个子图

sns.boxplot(x = "species",y = "petal_width",data = df,ax = axes[0]) #左图

#sns.boxplot(x = "species",y = "petal_width",data = df, palette="Set3", ax = axes[1]) #右图

sns.boxplot(x = "species",y = "petal_length",data = df, palette="Set2", ax = axes[1]) #右图