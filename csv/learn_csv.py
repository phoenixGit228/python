#%%
# 模块相关总结
import ...
import 模块名
from ... import ...
from(模块名) import (属性、函数、类)
if __name__ == '__main__'
# 通常用在主模块中使用。表示“程序入口”
# 当该程序是被导入运行时，该语句之后的代码不会执行

#%%
# 读取csv文件
import csv
with open('test.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#%%        
# 读取csv文件
import csv
before = input("请输入需要修改的字符串：")
after = input('请输入需要改为：')
csv_file = open('jobui2.csv', 'w', newline='')
writer = csv.writer(csv_file)
with open('jobui.csv', 'r',newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        list_row = []
        for i in row:
            if before in i:
                i = i.replace(before, after)
            list_row.append(i)
        writer.writerow(list_row)
csv_file.close()

#%%
import csv, os

csv_file = 'jobui.csv'
before = input("请输入需要修改的字符串：")
after = input('请输入需要改为：')

temp_file = open('temp.csv', 'w', newline='')
writer = csv.writer(temp_file)
with open(csv_file, 'r',newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        list_row = []
        for i in row:
            if before in i:
                i = i.replace(before, after)
            list_row.append(i)
        writer.writerow(list_row)
temp_file.close()
os.replace('temp.csv',csv_file)

#%%
# 学习csv模块
import csv
with open('test.csv', 'a', newline='') as f:
    writer = csv.writer(f)  # 创建实例
    writer.writerow([1, 2, 3, 4, 5])
    