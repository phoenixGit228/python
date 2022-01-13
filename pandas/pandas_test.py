import numpy as np
import pandas as pd

# 2-dimension list
# data = [['alex', 12], ['bob', 13]]
# df = pd.DataFrame(data, columns=['Name', 'Age'], index=['rank1', 'rank2'])
# print(df)

# dictionary
# data = [{'Name': 'Alex', 'Age': 12},
#         {'Name': 'Bob', 'Age': 13, 'Phone': '53654435'}, {'Name': 'Jack', 'Age': 18}]
# df = pd.DataFrame(data)
# print(df)

# df = pd.read_csv('./testing_data.csv', header=0)
# print(df)
# print(df.head(5))
# print(df['PDI2104_PV'])
# print(df[['PDI2104_PV', 'FIC1101_PV']])

# df = pd.DataFrame(np.arange(12).reshape(4, 3), index=[
#                   'x1', 'x2', 'x3', 'x4'], columns=['y1', 'y2', 'y3'])
# 取列
# print(df)
# print('---------')
# print(df[['y1', 'y3']])
# print('---------')
# 取行
# print(df.loc['x2':'x4'])
# print('---------')
# print(df.loc['x2', ['y1', 'y2', 'y3']])
# print('---------')
# # 列只能','分隔，行可以使用':'
# print(df.loc['x2':'x4', ['y1', 'y2', 'y3']])
# print('---------')
# print(df['x2':'x4'])
# print('---------')
# print(df['x2':'x4'][['y1', 'y3']])
# print('---------')
# print(df[['y1', 'y3']]['x2':'x4'])
# print('---------')
# print(df[['y1', 'y3']]['x2':'x2'])
# print('---------')
# print(df[['y1', 'y3']])
# print('---------')
# # 不能跳着取行
# # print(df['x1', 'x3'][['y1', 'y3']])
# # 与, 或, 非
# print(df[(df['y1'] >= 6) & (df['y2'] < 8)])
# print('---------')
# print(df[(df['y1'] >= 6) | (df['y2'] < 8)])
# print('---------')
# print(df[~(df['y2'] < 8)])
# print('---------')
# print(df[(df['y2'] < 8)]['x2':'x3'])
# print('---------')
# print(df.mean())
# print(df.mean(axis=1))

# df = pd.read_csv('testing_data.csv', header=0)
# print(df)
# print(df.head(2))
# print(df['PDI2104_PV'].sum())
# print(df['PDI2104_PV'].mean())

import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5, 6]
# y = [2.3, 4.2, 6.5, 4.3, 2.6, 1.8]

# plt.scatter(x, y, alpha=50, s=100, color='green', marker='+')
# plt.show()

x = np.random.uniform(0, 100, 100)
x.sort()
y = x ** 2 + 10
plt.scatter(x, y, color='green', alpha=0.5)
plt.show()
