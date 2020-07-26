#%%
with open(r'测试.csv', 'r', encoding='gbk') as file1:
    data = file1.read()
print(type(data))
with open('test.csv', 'w', encoding='gbk') as file2:
    file2.write(data)

#%%
info = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = []

# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引
# 序列，同时列出数据和数据下标，一般用在 for 循环当中。
for index, i in enumerate(info):
    # print(i + 1)
    print(index, end=" ")
    b.append(i + 1)

for index, i in enumerate(info):
      b.append(info[index]+1)

#%%
# 列表生成式
info = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = [x+1 for x in info] 
print(a)

#%%
lis = [x * x for x in range(10)]
print(lis)
print(type(lis))

generator_ex = (x * x for x in range(10))
print(generator_ex)
print(type(generator_ex))
print(next(generator_ex))
print(next(generator_ex))

#%%
import time
def consumer(name):
    print("%s 准备学习啦!" %name)
    while True:
        lesson = yield
        print("开始[%s]了,[%s]老师来讲课了!" %(lesson,name))

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("同学们开始上课 了!")
    for i in range(10):
        time.sleep(1)
        print("到了两个同学!")
        c.send(i)
        c2.send(i)


# %%
def create_counter(n):
    print("create_counter")
    while True:
        yield n
        print("increment n")
        n +=1

gen = create_counter(2)
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))

# %%
list1 = [10, 2, 3, 4]
list2 = str(list1)
print(type(list1))
print(type(list2))
print(type(list2[0]))
print(list2[0])
print(list2[1])
print(list2[2])
print(list2[3])
print(list2)


# %%
from selenium import webdriver
import time
# from selenium.webdriver.edge.webdriver import WebDriver as ChromiumEdge
driver = webdriver.ChromiumEdge()
time.sleep(2)
driver.get('https://www.baidu.com')
time.sleep(2)
driver.close()

# %%
import csv
csv_file = 'SEPDB.csv'

with open('SEPDB.csv', 'r',encoding='gbk') as file1:
    reader = csv.reader(file1)
    temp = []
    for i in reader:
        temp.append(i)
        if i[3] > 0.5:
            reader[i + 1][3] = 1
            temp.append(reader[i+1])
        i += 1

with open('sepdb2.csv', 'r', encoding='gbk') as file2:
    writer = csv.writer(file2)
    for i in temp:
        writer.writerow(i)




#%%
# !随机四位提取码
import random
lista=[]
for i in range(10):
    lista.append(str(i))
for i in range(65, 91):
    lista.append(chr(i))
for i in range(97, 123):
    lista.append(chr(i))
for i in range(10):
    print(''.join(random.sample(lista,4)))

# print(''.join(random.sample(lista,4)))


# %%
# !随机四位提取码
import random
list_a = [str(x) for x in range(10)]
list_b = [chr(i) for i in range(65, 91)]
list_c = [chr(i) for i in range(97, 123)]

# 循环输出10个4位提取码
for i in range(10):
    print(''.join(random.sample(list_a + list_b + list_c, 4)))

# print(''.join(random.sample(list_a + list_b + list_c, 4)))

#%%
# !随机四位提取码
#方法三
import string,random
code = ''.join(random.sample((string.digits+string.ascii_letters),4))
#random.sample(x,y)：从字符 x 中抽取 y 个随机字符
print('提取码：',code)
# print(string.digits[0:3])


