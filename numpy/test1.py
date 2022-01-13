#%%
# 导入numpy模块
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float)
print(a)
print('number of dim: ', a.ndim)
print('shape: ', a.shape)
print('size: ', a.size)
print(a.dtype)
#生成全是0的矩阵
b = np.zeros((3, 4))
print(b)
#生成全是1的矩阵
c = np.ones((3, 4))
print(c)
# 输出empty
print('输出empty矩阵')
d = np.empty((3, 4))
print(d)
#arange(初始值，不包含结束值，步长-可选)，步长默认为1
a = np.arange(10, 20, 2)
print(a)
a = np.arange(10, 20)
print(a)
a = np.arange(12).reshape((3,4))
print(a)
a = np.linspace(1, 10, 20).reshape(4,5)
print(a)

#%%
import numpy as np
a = np.array([10, 20, 30, 40])
b = np.arange(4)
print(b)
print(b < 3)

c = a + b
print(c)
c = b ** 2
print(c)
c = np.sin(a)
print(c)

# %%
import numpy as np
a = np.array([[1, 1],
              [0, 1]])
b = np.arange(4).reshape(2, 2)
print(a)
print('输出b')
print(b)
c = a * b
c_dot = np.dot(a, b)
print('输出c')
print(c)
print('输出c_dot')
print(c_dot)
c_dot = a.dot(b)
print('输出c_dot')
print(c_dot)


# %%
import numpy as np
a = np.random.random((2, 4))
print(a)
# axis=0 列，axis=1 行
print(np.sum(a,axis=0))
print(np.min(a, axis=1))
print(np.max(a, axis=0))

# %%
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





# %%
