# -*- coding: utf-8 -*-

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
#（1）导入数据
wine = load_wine()
X, y = wine.data, wine.target
#（2）分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
#（3）数据预处理
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
#（4）导入神经网络模型
from sklearn.neural_network import MLPClassifier
#（5）构建模型：使用一层网络
model = MLPClassifier(solver = "lbfgs",hidden_layer_sizes=(10,10))
#（6）训练神经网络模型
model.fit(X_train, y_train)
#（7）在训练集合和测试集合做预测
y_predict_on_train = model.predict(X_train)
y_predict_on_test = model.predict(X_test)
#（8）模型评估：查看预测准确率
from sklearn.metrics import accuracy_score
print('训练集合的准确率为: {:.2f}%'.format(100 * accuracy_score(y_train, y_predict_on_train)))
print('测试集合的准确率为: {:.2f}%'.format(100 * accuracy_score(y_test, y_predict_on_test )))

