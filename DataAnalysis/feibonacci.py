# %%
import numpy as np


def feibonacci(n):
    a, b = 1, 0
    while n > 0:
        print(a, end='  ')
        a, b = a+b, a
        n -= 1


feibonacci(100)


# %%
# !使用yield生成器
def fib_loop_while(max):
    a, b = 0, 1
    while max > 0:
        a, b = b, a + b
        max -= 1
        yield a


for i in fib_loop_while(10):
    print(i)
# %%
# ! 方法3

# 1


def fib_matrix(n):
    for i in range(n):
        res = pow((np.matrix([[1, 1], [1, 0]], dtype='int64')),
                  i) * np.matrix([[1], [0]])
        print(int(res[0][0]))


# 调用
fib_matrix(50)

# 2
# 使用矩阵计算斐波那契数列


def Fibonacci_Matrix_tool(n):
    Matrix = np.matrix("1 1;1 0", dtype='int64')
    # 返回是matrix类型
    return np.linalg.matrix_power(Matrix, n)


def Fibonacci_Matrix(n):
    result_list = []
    for i in range(0, n):
        result_list.append(np.array(Fibonacci_Matrix_tool(i))[0][0])
    return result_list


# 调用
Fibonacci_Matrix(50)

# %%
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city.title())
    print(city.upper())
    print(city.lower())


# %%
