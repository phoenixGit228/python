#同样，运行后重新打开文件查看变化
import os

list_test = ['一弦一柱思华年。\n','只是当时已惘然。\n']

with open ('poem1.txt','r',encoding='utf8') as f:
    lines = f.readlines()

with open('poem2.txt','w',encoding='utf8') as new:
    for line in lines:
        if line in list_test:
            new.write('____________。\n')
        else:
            new.write(line)

# os.replace('poem2.txt', 'poem1.txt')

# os.getcwd()  # 返回当前工作目录
# os.listdir(path)   # 返回path指定的文件夹包含的文件或文件夹的名字的列表
# os.mkdir(path)  # 创建文件夹
# os.path.abspath(path)   # 返回绝对路径
# os.path.basename(path)   # 返回文件名
# os.path.isfile(path)   # 判断路径是否为文件
# os.path.isdir(path)   # 判断路径是否为目录
