# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 21:30:45 2019

@author: Yuhong
"""

from sklearn.datasets import fetch_mldata
from sklearn.linear_model import LogisticRegression

mnist = fetch_mldata("MNIST original")

from sklearn.model_selection import train_test_split
train_img, test_img, train_lbl, test_lbl = train_test_split(mnist.data, mnist.target, 
                                                            test_size = 1/7.0, random_state = 0)
logisticRegr = LogisticRegression()
logisticRegr.fit(train_img, train_lbl)

logisticRegr.predict(test_img[0].reshape(1,-1))
#预测一批数据的分类
predictions = logisticRegr.predict(test_img)
#accuracy
score = logisticRegr.score(test_img, test_lbl)
print(score)
