#!/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(style="ticks")

iris = pd.read_csv('iris.csv',header=None)
iris.columns=['sepal_length','sepal_width',
              'petal_length','petal_width','species']

sns.pairplot(iris,hue="species",diag_kind="kde",
             palette="muted")
plt.show()
