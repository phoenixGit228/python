"""

学习 Pandas

"""
#
"""
第一部分
Import the package, import pandas as pd
A table of data is stored as a pandas DataFrame
Each column in a DataFrame is a Series
You can do things by applying a method to a DataFrame or Series
"""

# %%
"""
存储数据进表格, 创建一个DataFrame.
"""
import pandas as pd
# print(dir(pd))
df = pd.DataFrame({
                    "Name": ["Braund, Mr. Owen Harris",
                    "Allen, Mr. William Henry",
                    "Bonnell, Miss. Elizabeth"],
                    "Age": [22, 35, 58],
                    "Sex": ["male", "male", "female"]}
                )

df

# %%
"""
To select the column, use the column label in between square brackets []

类似与字典，通过键选择值
"""
df['Age']

# %%
"""
create a Series from scratch as well
A pandas Series has no column labels, as it is just a single column of a DataFrame. A Series does have row labels

Series相当于DataFrame中的一列，但没有列标签，也没有行标签
"""
ages = pd.Series([25,30,20],name = 'Age')
ages

# %%
"""
操作DataFrame和Series，两者都有很多方法，不要忘记方法最后的()

As illustrated by the max() method, you can do things with a DataFrame or Series. pandas provides a lot of functionalities, each of them a method you can apply to a DataFrame or Series. As methods are functions, do not forget to use parentheses ()
"""
df['Age'].max()

# %%
"""
操作DataFrame和Series
"""
ages.max()

# %%
"""
读写文件
pandas provides the read_csv() function to read data stored as a csv file into a pandas DataFrame. pandas supports many different file formats or data sources out of the box (csv, excel, sql, json, parquet, …), each of them with the prefix read_*.
import pandas as pd
"""
test = pd.read_csv("test2.csv")
test

# %%
"""
Make sure to always have a check on the data after reading in the data. When displaying a DataFrame, the first and last 5 rows will be shown by default
#数据量较大时，默认显示前5行和后5行，最好检查下数据是否正确
"""
import pandas as pd
test = pd.read_csv("齐鲁20200111-20200118测试用500.csv", encoding='GBK')
test

# %%
"""
To see the first N rows of a DataFrame, use the head() method with the required number of rows (in this case 8) as argument.
显示数据前8行
"""
test.head(8)

# %%
"""
A check on how pandas interpreted each of the column data types can be done by requesting the pandas dtypes attribute:
dtypes is an attribute of a DataFrame and Series. Attributes of DataFrame or Series do not need brackets.

检查各列的数据类型，使用dtypes属性，不需要加括号()
"""
# test.dtypes
test['PDI2104_PV'].dtypes

# %%
"""
读取Excel文件，使用 read_excel
参数项sheet_name可选，读取特定sheet，默认选择第一个sheet
默认第一行作为列名
"""
import pandas as pd
data = pd.read_excel('test.xlsx',sheet_name='Sheet1')
data  # 整个data DataFrame表格

# %%
"""
前N行，使用head(N)，如果留空，默认前5行
后N行，使用tail(N)，如果留空，默认后5行
"""
data.head(3)  # data前3行
# test.tail(3)

# %%
'''
Whereas read_* functions are used to read data to pandas, the to_* methods are used to store data. The to_excel() method stores the data as an excel file. In the example here, the sheet_name is named passengers instead of the default Sheet1. By setting index=False the row index labels are not saved in the spreadsheet.

相对于read_*()是读取方法，to_*()是保存数据到某种格式
index = False, 行序号不会保存在新的excel里面'''

data.to_excel('test2.xlsx', sheet_name='sheet2', index=False)
data2 = pd.read_excel('test2.xlsx',sheet_name='sheet2')
data2

# %%
import pandas as pd
test = pd.read_excel(r"C:\coding\py\pandas\test.xlsx", encoding='GBK')
test.info()
# test

# %%
import pandas as pd
test = pd.read_csv("齐鲁20200111-20200118测试用500.csv", encoding='GBK')
# test.info()

'''
DataFrame.shape is an attribute (remember tutorial on reading and writing, do not use parantheses for attributes) of a pandas Series and DataFrame containing the number of rows and columns: (nrows, ncolumns). A pandas Series is 1-dimensional and only the number of rows is returned.

shape属性返回DataFrame结果（n行，m列）
series 是一维的，只有行返回值'''

test['Time'].shape

# %%
'''
选择数据的特定列
内部的[]用于定义一个list，外部的[]是选择DataFrame'''

data = test[['Time', 'PDI2104_PV']]
data
type(data)
data.shape  # 返回结果，152590行, 2列
data.info()

# %%
'''
选择特定行,在[]中添加条件
To select rows based on a conditional expression, use a condition inside the selection brackets [].
The condition inside the selection brackets data['PDI2104_PV'] > 60 checks for which rows the PDI2104_PV column has a value larger than 60
The output of the conditional expression (>, but also ==, !=, <, <=,… would work) is actually a pandas Series of boolean values (either True or False) with the same number of rows as the original DataFrame. Such a Series of boolean values can be used to filter the DataFrame by putting it in between the selection brackets []. Only rows for which the value is True will be selected.

通过条件表达式数值类型——整型、浮点型（>, but also ==, !=, <, <=），字符串型（True，False）选择特定行'''
above_60 = data[data['PDI2104_PV'] > 60]
above_60.shape

# %%
# isin() 也是条件表达式，类似与python中的in，not in
import pandas as pd
col = pd.read_excel('test2.xlsx',encoding ='GBK')
col
'''
class_23 = col[(col["col1"] == 2) | (col["col1"] == 3)] 和下面表达式等价

多个条件必须在[]中使用()分隔开，与操作符为 &,或操作符为 |
'''
class_23 = col[col["col1"].isin([2, 3])]
class_23

# %%
'''
The notna() conditional function returns a True for each row the values are not an Null value. As such, this can be combined with the selection brackets [] to filter the data table.
DataFrame['column_name'].notna()

数据非空'''
import pandas as pd
test = pd.read_csv("安庆历史数据20190516-20190708.csv", encoding = 'GBK')
# test.head()
# test.info()
no_na = test[test["LIC5102_MV"].notna()]
no_na
no_na.shape
no_na['LIC5102_MV']

# %%
'''
When selecting subsets of data, square brackets [] are used.
Inside these brackets, you can use a single column/row label, a list of column/row labels, a slice of labels, a conditional expression or a colon.
Select specific rows and/or columns using loc when using the row and column names
Select specific rows and/or columns using iloc when using the positions in the table
You can assign new values to a selection based on loc/iloc.

选择特定行，特定列'''

import pandas as pd
test = pd.read_csv("安庆历史数据20190516-20190708.csv", encoding='GBK')
data = test.loc[test["PDI2104_PV"]> 60, ["FIC1101_PV","FIC1102_PV"]]
data

'''
[行，列] 其中的行和列可以使用 m:n 从第m行到第n行，从第m列到第n列
DataFrame.iloc[行，列] 取值，特定行，特定列，只能是数字，'''

data = test.iloc[20:30,1:5]
data

'''
DataFrame.loc[行号，列（可以是数字，也可以是列名）]
'''
data = test.loc[20:30,["Time",'PDI2104_PV']]
data

# iloc()指定特定列的特定行为指定值
# test.iloc(行:行，列) = 指定值
# test.iloc(行，列：列) = 指定值
# test.iloc[30:, 10] = 5
test.iloc[2:, 1:5] = 5
test.info()
test

# %%
# 利用pandas画图
import pandas as pd
import matplotlib as plt
test = pd.read_csv("test2.csv", index_col=0)
test.head()


# %%
'''
The usage of the index_col and parse_dates parameters of the read_csv function to define the first (0th) column as index of the resulting DataFrame and convert the dates in the column to Timestamp objects, respectively.

使用index_col将数据的第一列作为索引列，使用parse_dates将数据转为时间格式
'''
import pandas as pd
import matplotlib.pyplot as plt

test = pd.read_csv("齐鲁20200111-20200118测试用500.csv", index_col = 0,parse_dates=True)

'''
With a DataFrame, pandas creates by default one line plot for each of the columns with numeric data.

pandas默认将每列画一条线'''

plt.rcParams['font.sans-serif'] = ['SimHei']  #显示中文
test.plot(figsize = (12,12))
# test[['PDI2104_PV','FIC1101_PV',"FIC1102_PV"]].plot(figsize = (12,12))

# %%
# 绘制特定列的数据
listx = ['PDI2104_PV','FIC1101_PV']
test[listx].plot()

# %%
# 绘制 x,y关系图
test.plot.scatter(x="FIC1101_PV", y = "FIC1102_PV", alpha = 0.5)

# %%
import pandas as pd
import matplotlib.pyplot as plt
test = pd.read_csv("test2.csv",index_col=0, parse_dates=True)

# %% 所有列绘图
test.plot()

# %% 特定列绘图，如果是多列绘图，[]多个内必须是一个列表
test[['x','y']].plot()

#%%
'''
绘制x-y关系图，x-x轴，y- y轴，默认用列名作为坐标轴名字，alpha 可选，默认为1，透明度，0-1
'''
test.plot.scatter(x='x', y='y',alpha = 0.5)

# %%
'''
Apart from the default line plot when using the plot function, a number of alternatives are available to plot data. Let’s use some standard Python to get an overview of the available plot methods:

默认使用直线绘图，也可以用其他方式绘图，下面列出其方法'''

[method_name for method_name in dir(test.plot)
    if not method_name.startswith("_")]
# 结果为 ['area', 'bar', 'barh', 'box', 'density', 'hexbin', 'hist', 'kde', 'line', 'pie', 'scatter']
# 面积图，条形图，。。。
test.plot.box()
# subplots参数用于分开绘制
test.plot.area(figsize = (12,12),subplots = True)
test.plot.bar(subplots=True)
test.plot.barh()
# test.plot.density()
# test.plot.hexbin(x = 'x', y ='y')
# test.plot.hist()
# test.plot.kde()
# test.plot.line()
# test.plot.pie(subplots= True)
# test.plot.scatter(x='x', y='z')

# %%
# Create an empty matplotlib Figure and Axes
fig,axs = plt.subplots(figsize=(12,8))
# Use pandas to put the area plot on the prepared Figure/Axes
test.plot.area(ax = axs)
# Do any matplotlib customization you like
axs.set_ylabel("co")
# Save the Figure/Axes using the existing matplotlib method.
fig.savefig("co_concentrations.png")

'''
The .plot.* methods are applicable on both Series and DataFrames
By default, each of the columns is plotted as a different element (line, boxplot,…)
Any plot created by pandas is a Matplotlib object.
'''
# %%
import pandas as pd
import matplotlib.pyplot as plt
test = pd.read_csv(".\安庆历史数据20190516-20190708.csv",index_col =0,parse_dates=True)
# test
# test['PDI2401_PV']
# test[['Time', 'PDI2104_PV','FIC1101_PV','FIC1102_PV']]
data = test[['PDI2104_PV','FIC1101_PV','FIC1102_PV']]
# data
data.to_csv('testing_data.csv',index = True)
# data.to_csv('testing_data2.csv')  # 如果index = False未添加，默认会在左列添加一列行号

# %%
import pandas as pd
air_quality = pd.read_csv('.\data\\air_quality_no2.csv',index_col=0, parse_dates = True)
# air_quality = pd.read_csv('.\data\\air_quality_no2.csv')
air_quality.head()
'''
To create a new column, use the [] brackets with the new column name at the left side of the assignment.
Also other mathematical operators (+, -, *, /) or logical operators (<, >, =,…) work element wise. The latter was already used in the subset data tutorial to filter rows of a table using a conditional expression.

添加新的列，使用[]+新的名字即可，类似与字典
这些值是一次性全计算，不需要迭代计算
'''
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
# 保存至文件
# air_quality.to_csv('.\data\\air_quality_no2_london.csv',index = True)
air_quality["ratio_paris_antwerp"] = air_quality["station_paris"]/ air_quality["station_antwerp"]
air_quality

# %%
'''
The rename() function can be used for both row labels and column labels. Provide a dictionary with the keys the current names and the values the new names to update the corresponding names.

rename()方法，可以修改行标签和列标签，用法比较类似与字典，使用冒号: 左侧当前名字，右侧新名字'''
air_quality_renamed = air_quality.rename(columns=
    {"station_antwerp": "BETR801",
    "station_paris": "FR04014",
    "station_london": "London Westminster"})
air_quality_renamed.head()

# %%
import pandas as pd
titanic = pd.read_csv(r'C:\coding\py\pandas\data\titanic.csv')
titanic['Age'].mean()
titanic['Age'].median()
titanic['Fare'].median()

# DataFrame.describe()方法可用于更多统计信息展示
titanic[['Age', 'Fare']].describe()

# using the DataFrame.agg() method:
# 指定统计方法使用DataFrame.agg()方法
titanic.agg({"Age": ["mean", "min", "max","skew"], "Fare": ["mean", "min", "max","count"]})

# 更进一步的分类统计.Groupby("column_name").方法

# titanic[["Sex", "Age"]].groupby("Sex").mean()
titanic[["Sex", "Age","Fare"]].groupby("Sex").mean()
titanic.groupby("Sex").mean()
titanic['Pclass'].value_counts()
titanic.groupby('Pclass')["Pclass"].count()

# %%
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('testing_data.csv',index_col = 0,parse_dates = True)
data["PDI2104_mean"] = data["PDI2104_PV"].mean()
data["PDI2104_max"] = data["PDI2104_PV"].max()
data["PDI2104_min"] = data["PDI2104_PV"].min()
data[["PDI2104_PV", "PDI2104_max", "PDI2104_min", "PDI2104_mean"]].plot()
data.info()

# %%
'''
.sort_values(by = "",ascending= True/False) ascending True，升序，False降序排列
'''
import pandas as pd
titanic = pd.read_csv(r'C:\coding\py\pandas\data\titanic.csv')
titanic.sort_values(by = "Age")
titanic.sort_values(by = "Age",ascending=False)
titanic.sort_values(by= ["Pclass", "Age"],ascending = True)

# %%
import pandas as pd
air_quality = pd.read_csv(".\data\\air_quality_long.csv",index_col = "date.utc", parse_dates = True)
air_quality
air_quality.sort_values(by="date.utc", )

# %%
'''
filter for no2 data only
数据过滤
'''
no2 = air_quality[air_quality["parameter"] == "no2"]
no2

# %%
# use 2 measurements (head) for each location (groupby)
no2_subset = no2.sort_index().groupby(["location"]).head(2)
no2_subset.info()
no2_subset

# %%
