import numpy as np
import pandas as pd

df = pd.read_csv('./students_complete.csv',
                 encoding='utf-8', header=0)
print(df.head(10))
math_mean = df['math_score'].mean()
print('-------------------------------------')
print(f'学生数学平均分为：{math_mean:>10.1f}')
# math_loss = df[df['math_score'] < 60].size #这是数组所有元素个数
math_loss = df[df['math_score'] < 60]['Student ID'].count()
print(f'数学未及格人数：{math_loss:>12}')
print('-------------------------------------')
print('各学校数学平均分：')
df_group = df.groupby('school_name')
print(np.around(df_group['math_score'].agg('mean'), decimals=1))
