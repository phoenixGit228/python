'''
Author:     DunMin SONG
organization: 光环国际
Project:    regression_model
software:   PyCharm
'''

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
# 加载数据集
diabetes = datasets.load_diabetes()
# print("origin")
# print(diabetes.data[0:5])
# print("newaxis")
# print(diabetes.data[0:5, np.newaxis])

# Use only one feature # np.newaxis will add a new axis 
# for the data
# diabetes_X = diabetes.data[:, np.newaxis, 2]
print(diabetes)
diabetes_X = diabetes.data

# print(diabetes_X[0:5])
# print(diabetes_X[0,0])

# 随机取数
# diabetes_X_train, diabetes_X_test, diabetes_y_train, diabetes_y_test = train_test_split(diabetes_X, diabetes.target, test_size=0.05)

# Split the data into training/testing sets
#用不同的特征训练
diabetes_X = diabetes_X[:,8].reshape(-1,1)
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]
'''
'''
# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
print(diabetes_X_train)
print(diabetes_y_train)

regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)
score = regr.score(diabetes_X_test,diabetes_y_test)
print(score)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))

# # Plot outputs
# plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
# plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

# plt.xticks(())
# plt.yticks(())

# plt.show()

## 思考，是否可以判断数据的噪声
