# file1 = open('./abc.txt', 'a', encoding='utf-8')
# file1.write('张无忌\n')
# file1.write('宋青书\n')
# file1.close()
# file1 = open('./abc.txt', 'r', encoding='utf-8')
# filecontent = file1.read()
# print(filecontent)
# file1.close()

with open('scores.txt', 'r', encoding='utf-8') as files1:
    file_lines = files1.readlines()
    # print(file_lines)

final_score = []

for i in file_lines:
    data = i.split()
    # print(i)
    # print(data)
    data_score = 0
    for j in data[1:]:
        data_score = data_score + float(j)
    result = data[0] + str(data_score) + '\n'
    # print(result,end=' ')
    final_score.append(result)

with open('winner.txt', 'w+', encoding='utf-8') as winner:
    winner.writelines(final_score)