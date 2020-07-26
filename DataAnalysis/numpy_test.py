# %%
# import numpy as np
# a = np.arange(15).reshape(3, 5)
# a.shape
# a.ndim
# a.dtype.name
# a.itemsize
# a.size
# b = np.array([6, 7, 8])
# b
# type(b)

# arr1 = np.array([1, 2, 3, 4])
# print(arr1)

# arr_tuple = np.array((1, 2, 3, 4))
# print(arr_tuple)

# # 二维数组
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr2)

# arr1 = np.arange(5)
# print(arr1)
# arr2 = np.array([np.arange(5), np.arange(5)])
# print(arr2)
# arr3 = np.arange(5, dtype=float)
# print(arr3)


# data = np.genfromtxt('./data_numpy.csv', delimiter=',', dtype=int)
# print(data)
# print(data.ndim)
# print(data.shape)
# print(data.size)
# a = np.arange(7)
# a
# # 数组切片
# a[1:4]
# a[:6:2]
# a[::2]
# print(data[0:3, 2:5])
# # 数组变形
# print(data.reshape(5, 4))
# data.resize(5, 4)
# print(data)
# # 数组降成一维
# print(data.flatten())
# print(data)
# print(data.ravel())
# print(data)
# # 数组求值
# print(np.sum(data[:2]))
# print(np.mean(data[:2]))
# print(np.max(data[:2]))
# print(np.min(data[:2]))
# print(data.min())
# # 计算每行的值
# print(data.sum(axis=1))
# print(np.sum(data, axis=1))
# # 计算每列的值
# print(data.sum(axis=0))


# print(data.reshape(2, 2, 5))

# %%
# 第三题
import numpy as np
score = float(input('请输入学生成绩：'))
if score >= 90:
    print('该生成绩A')
elif score >= 70:
    print('该生成绩B')
elif score >= 60:
    print('该生成绩C')
else:
    print('该生成绩D')

# %%
# 第四题
# 第一种方法
size = int(input('please input your array size: '))
arr = []
for x in range(size):
    num = int(input(f'please input number array[{x}]: '))
    arr.append(num)
print('数组修改前：')
print(arr)
max_num = arr[0]
max_index = 0
for i in range(len(arr)):
    if max_num <= arr[i]:
        max_index = i
print(max_index)
arr[0], arr[max_index] = arr[max_index], arr[0]
print(arr)

min_num = arr[0]
min_index = 0
for i in range(len(arr)):
    if min_num >= arr[i]:
        min_index = i
print(min_index)
arr[-1], arr[min_index] = arr[min_index], arr[-1]

print('数组修改后：')
print(arr)

# %%
# 第四题
# 第二种方法
size = int(input('please input your array size: '))
arr = []
for x in range(size):
    num = int(input(f'please input number array[{x}]: '))
    arr.append(num)

print('数组修改前：')
print(arr)
max_num = max(arr)
max_index = arr.index(max_num)
arr[0], arr[max_index] = arr[max_index], arr[0]
min_num = min(arr)
min_index = arr.index(min_num)
arr[-1], arr[min_index] = arr[min_index], arr[-1]
print('数组修改后：')
print(arr)

# %%
# 第四题
# 第三种方法
size = int(input('please input your array size: '))
arr = []
for x in range(size):
    num = int(input(f'please input number array[{x}]: '))
    arr.append(num)

print('数组修改前：')
print(arr)
# max_num = max(arr)
# max_index = arr.index(max_num)
arr[0], arr[arr.index(max(arr))] = arr[arr.index(max(arr))], arr[0]
# min_num = min(arr)
# min_index = arr.index(min_num)
print(arr)
arr[-1], arr[arr.index(min(arr))] = arr[arr.index(min(arr))], arr[-1]
print('数组修改后：')
print(arr)

# %%
# 第五题

arr = np.arange(36).reshape(4, 9)
print(arr)
# 输出每一行的平均值
print('每一行的平均值')
print(arr.mean(axis=1))
# 输出每一列的平均值
print('每一列的平均值')
print(arr.mean(axis=0))
