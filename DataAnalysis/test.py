# %%
sum = 0
for x in range(0, 10, 2):
    print(x)
    sum += x
print(sum)

# %%
for i in range(5):
    for j in range(4):
        print("outer index i: {}, inner index j: {}".format(i, j))

# %%
limit = 40
num = 0
while (num + 1) ** 2 < limit:
    num += 1

nearest_square = num ** 2
print(nearest_square)

# %%
website = "http://yun.aura.com"
for x in website:
    if x == 'c':
        continue
    print(x, end='')

# %%
website = "http://yun.aura.com"
for x in website:
    print(x, end='')
    continue
    # if x == 'c':

# %%
for num in range(1000, 2000):
    if (num % 4 == 0 and num % 100 != 0) or num % 400 == 0:
        print(f'{num}是闰年')

# %%


def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2


print(cylinder_volume(10, 3))
print(cylinder_volume(10))

# %%
# 阶乘 5！=5*4*3*2*1


def myfac(n):
    if n == 1:
        return 1
    else:
        return n * myfac(n - 1)


num = int(input('please input an integer:'))
print(myfac(num))

# %%
fd = open('./demo.py', 'r', encoding='utf-8')
print(fd.read())
fd.close()

# %%
fd = open('./demo.py', 'r', encoding='utf-8')
print(fd.readline())
print(fd.readline())
fd.close()

# %%
fd = open('./test.txt', 'w')
fd.write('hello world')
fd.close()

# %%
with open('./test.txt', 'w') as fd:
    fd.write('hello world')

with open('test.txt', 'r') as file1:
    