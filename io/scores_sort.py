# 下面已经为你准备好了打开的代码和一些变量名的准备。
# 请你完成数据处理以及新建文档（同一个目录）的代码。
# 一个提示：可以用 print 作为检验代码，步步为营。

file1 = open('winner.txt','r',encoding='utf-8') 
file_lines = file1.readlines() 
file1.close()

# print(file_lines)

dict_scores = {}
list_scores = []
final_scores = []

for i in file_lines:
    data = i.split()
    str1 = data[0]
    # print(str1)
    dict_scores[str1[:-3]] = int(str1[-3:])
    list_scores.append(int(str1[-3:]))

# print(dict_scores)
# print(list_scores)

def get_keys(value, list1):
    for keys in list1:
        if value == list1[keys]:
            return keys
        
list_scores.sort(reverse=True) # 降序排列
# print(list_scores)

for i in list_scores:
    keys = get_keys(i, dict_scores)
    result = keys + str(i) +'\n'
    final_scores.append(result)

print(final_scores)

sum1 = open('winner_new.txt','w',encoding='utf-8') 
sum1.writelines(final_scores)
sum1.close()
