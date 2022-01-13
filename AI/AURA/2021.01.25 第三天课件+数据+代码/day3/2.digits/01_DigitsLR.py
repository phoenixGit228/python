'''
Author:     DunMin SONG
organization: 光环国际
Project:    regression_model
software:   PyCharm
'''
# 导入numpy科学计算库
import numpy as np
# 导入数据集、线性回归模型
from sklearn import datasets, neighbors, linear_model
from sklearn.model_selection import train_test_split
# 获取手写数字识别模型
digits = datasets.load_digits()
# 获取特征
X_digits = digits.data
# 获取标签
y_digits = digits.target
# print(X_digits)
# print(y_digits)
# print(np.shape(X_digits))
# print(np.shape(y_digits))

# 获取样本数量
n_samples = len(X_digits)
# print(n_samples)

X_train, X_test, y_train, y_test = train_test_split(X_digits, y_digits, test_size=0.1)
'''
# 区分训练集和测试集，90%训练集，10%测试集
X_train = X_digits[:int(.9 * n_samples)]
y_train = y_digits[:int(.9 * n_samples)]
X_test = X_digits[int(.9 * n_samples):]
y_test = y_digits[int(.9 * n_samples):]
'''
#逻辑回归模型
logistic = linear_model.LogisticRegression(max_iter=3000)
# model = logistic.fit(X_train, y_train)
# y_pre = model.predict(X_test)
# score = model.score(X_test,y_test)
#
# print('LogisticRegression score: %f' % score)
#打印手写数字识别的准确率
print('LogisticRegression score: %f'
      % logistic.fit(X_train, y_train).score(X_test, y_test))
'''
'''