import pandas as pd
from sklearn.datasets import load_iris

#(1) 加载IRIS数据集合
iris = load_iris()
X = iris.data
y = iris.target
#(2)分割数据
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, 
random_state = 123)
#（3）选择模型
from sklearn.neighbors import KNeighborsClassifier
# (4)生成模型对象
knn = KNeighborsClassifier(n_neighbors = 3)
#（5）数据拟合（训练模型）
knn.fit(X,y)
#（6） 模型预测
#6.1 单个数据预测
knn.predict([[4,3,5,3]])  #输出array([2])
#6.2 大集合据预测
y_predict_on_train = knn.predict(X_train)
y_predict_on_test = knn.predict(X_test)
# （7）模型评估
from sklearn.metrics import accuracy_score
print('训练集合的准确率为: {:.2f}%'.format(100 * accuracy_score(y_train, y_predict_on_train)))
print('测试集合的准确率为: {:.2f}%'.format(100 * accuracy_score(y_test, y_predict_on_test )))

