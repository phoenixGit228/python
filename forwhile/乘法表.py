#%%
for i in range (1, 10):
    str1 = ''
    str2 = ''
    for j in range(1, i + 1):
        str1 = str(j) + ' X ' + str(i) + ' = ' + str(i*j)
        str2 += '  '
        str2 += str1
    print(str2)

#%% 九九乘法表
for i in range(1,10):
    for j in range(1, i+1):
        print('%s X %s = %2d' % (j, i, i*j), end='  ')
    print()

# %%
