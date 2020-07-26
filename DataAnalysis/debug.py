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
