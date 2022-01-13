'''
Author:     DunMin SONG
organization: 光环国际
Project:    Linear_Regression
software:   PyCharm
'''
# -*-coding:utf-8-*-
# 引入包
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# 管道
from sklearn.pipeline import Pipeline
# 多项式特征
from sklearn.preprocessing import PolynomialFeatures
# 标准化
from sklearn.preprocessing import StandardScaler
# 读取数据
data = np.load('covid-Usa.npz')
Usa = data['Usa']
#print(China)
X = np.arange(np.size(Usa)).reshape(-1, 1)
print(X)
print(Usa)
# 建立模型
Poly_Fe = Pipeline(steps=[('poly', PolynomialFeatures(degree=10)),# 特征扩展 degree是几次方
                          ('St_sc', StandardScaler()),          # 归一化 (x-均值)/方差
                          ('lr', LinearRegression())])          # 线性回归
# ctrl + alt + l 规范代码
# 训练模型
# y= k * x + b
Poly_Fe.fit(X,Usa)
# 预测、推断
y = Poly_Fe.predict(X)

# print(Poly_Fe.score(X,China))
#画图真实值
plt.scatter(X, Usa)
#解决中文标题的问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title("美国疫情数据分析")
# 预测值
plt.plot(X,y,color='r')
plt.show()
print(Poly_Fe.score(X,Usa))