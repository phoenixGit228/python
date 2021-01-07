#%%
count = 0
n = 0
for i in range(0, 100//7):
    for j in range(0, 100//3):
        for k in range(0, 100//2):
            # print(f"i = {i}, j = {j}, k = {k}")
            n+= 1
            if (i*7 +j*3 + k*2 == 100):
                count +=1
print(count)
print(n)

#%%
count = 0
n = 0
for i in range(0,100//7):
    for j in range(0,100//3):
            n+=1
            if not((100- i*7 +j*3)%2):
                count +=1
print(count)
print(n)
# %%
