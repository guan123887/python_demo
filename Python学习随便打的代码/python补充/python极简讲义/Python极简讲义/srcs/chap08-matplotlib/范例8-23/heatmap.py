#!/usr/bin/env python
# coding=utf-8

import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns

#iris = pd.read_csv('iris.csv',header=None)
#iris.columns=['sepal_length','sepal_width',
#              'petal_length','petal_width','species']
#iris_corr = iris.corr()
#sns.heatmap(wine_corr,annot=True,square=True,fmt='.2f', 
#            annot_kws={'size':150,'weight':'bold', 'color':'red'})

plt.figure(figsize=(40,20),dpi = 150)
wine = pd.read_csv('wine.csv')
wine_corr = wine.corr()
plt.figure(figsize=(20,10))
sns.heatmap(wine_corr,annot=True,square=True,fmt='.2f')
plt.show()

