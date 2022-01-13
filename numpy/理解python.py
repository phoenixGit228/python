#定义一维数组
import numpy as np
my_array = np.array([1, 2, 3, 4, 5])
print(my_array)
#数组大小
print(my_array.shape)
#打印数组元素
print(my_array[0])
print(my_array[1])
#修改数组元素
my_array[1] = -1
print(my_array)
#创建长度为5的Numpy数组
#所有元素全是0
my_new_array = np.zeros((5))
my_new_array
# print(my_new_array)
#所有元素全是1
my_new_array = np.ones((5))
my_new_array
# print(my_new_array)
#创建随机数数组
my_random_array = np.random.random((5))
print(my_random_array)
#创建二维数组
my_2d_array = np.zeros((2,3))
print(my_2d_array)
my_2d_array_new = np.ones((2, 4))
print(my_2d_array_new)

