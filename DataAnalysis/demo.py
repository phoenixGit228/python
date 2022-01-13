# # dict_value = {"Wuhan":[10000,rising],"Beijing":[2000,dec],......}
# dict1 = {1: 1000, 2: 2000, 3: 3000}
# # print(dict1[1])
# # print(dir(dict))
# # print(dir(list))
# # print(dir(tuple))
# print(dir(set))


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
