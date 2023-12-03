# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 20:21:22 2019

@author: Yuhong
"""

#(1)导入数据
#import pandas
import pandas as pd
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
# load dataset
pima = pd.read_csv("diabetes.csv", header=None, names=col_names)

#（2）分割特征和目标变量
feature_cols = ['pregnant', 'insulin', 'bmi', 'age','glucose','bp','pedigree']
X = pima[feature_cols] # 特征
y = pima.label # 目标
#（3）分割数据
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

#（4）模型选择和训练¶
# import the class
from sklearn.linear_model import LogisticRegression

# instantiate the model (using the default parameters)
logreg = LogisticRegression(solver='newton-cg')

# fit the model with data
logreg.fit(X_train,y_train)
y_pred=logreg.predict(X_test)

#(5)使用混淆矩阵来评估模型
from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print(cnf_matrix)

#（6）输出性能
print("准确率:{:.2f}".format(metrics.accuracy_score(y_test, y_pred)))
print("查准率:{:.2f}".format(metrics.precision_score(y_test, y_pred)))
print("查全率:{:.2f}".format(metrics.recall_score(y_test, y_pred)))

# (7)ROC曲线
import matplotlib.pyplot as plt
# 为在Matplotlib中显示中文，设置特殊字体
plt.rcParams['font.sans-serif']=['SimHei']
fig = plt.figure(figsize=(9, 6), dpi=100)
ax = fig.add_subplot(111)
y_pred_proba = logreg.predict_proba(X_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.plot(fpr,tpr,label="pima糖尿病, auc={:.2f}".format(auc))
plt.legend(shadow=True, fontsize=13, loc = 4)
plt.show()