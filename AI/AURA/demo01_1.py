'''
Author:     DunMin SONG
organization: 光环国际
Project:    Linear_Regression
software:   PyCharm
'''
# 引入包 numpy 科学计算使用
import numpy as np
# matplotlib画图
import matplotlib.pyplot as plt
# 引入线性回归模型
from sklearn.linear_model import LinearRegression

# 处理数据
Usa = []
# 读取CSV文件数据
with open(file='owid-covid-data.csv', mode='r', encoding='utf-8') as f:
    # 按行读取
    data = f.readlines()
    # 读取每个字段的值
    for line in data:
        # 按,分割字段
        field = [item for item in line.split(',')]
        # 将第2列等于 United States 的数据读取出来
        if field[2] == 'United States':
            #将数据添加到usa的数组里
            Usa.append(field[4])
# 将浮点数转化为整型
Usa = np.array(Usa, dtype=np.float).astype(int)
# 将处理好的数据保存下来
np.savez('covid-Usa',Usa=Usa)
# print(Usa)
# 构建X的值
X = np.arange(np.size(Usa)).reshape(-1, 1)
# 线性回归模型
model = LinearRegression()
# 训练模型
model.fit(X, Usa)
# 推断、预测
y = model.predict(X)
# w或者k
print(f"系数：model.coef_")
# b
print(f"截距：model.intercept_")
# y1 = 56595.32618688 * X  - 4276412.02377165
#画图
plt.scatter(X,Usa)
plt.plot(X,y,color='r')
# plt.plot(X,y1,color='g')
plt.show()
# 查看模型得分
print(model.score(X,Usa))
'''
'''