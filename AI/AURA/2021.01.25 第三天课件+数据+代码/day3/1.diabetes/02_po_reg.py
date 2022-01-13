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
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
# 加载数据集
diabetes = datasets.load_diabetes()

diabetes_X = diabetes.data


# 随机取数
# diabetes_X_train, diabetes_X_test, diabetes_y_train, diabetes_y_test = train_test_split(diabetes_X, diabetes.target, test_size=0.05)

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

pi_line = Pipeline([('poly', PolynomialFeatures(degree=1)),
                    ('st', StandardScaler()),
                    ('lr', LinearRegression())])

pi_line.fit(diabetes_X_train,diabetes_y_train)


diabetes_y_pred = pi_line.predict(diabetes_X_test)
score = pi_line.score(diabetes_X_test,diabetes_y_test)
print(score)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))