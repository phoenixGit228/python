# #########################################
#
# 文件: scores.py
# 描述: 从txt文件读取分数，求取最高成绩
# 日期: 2021-03-07 09:23:20
#
# ##########################################

file1 = open('scores.txt','r',encoding='gb2312') 
file_lines = file1.readlines() 
file1.close()

final_scores = []

for i in file_lines:
    data =i.split()
    sum = 0  # 先把总成绩设为0
    for score in data[1:]:  # 遍历列表中第1个数据和之后的数据
        sum = sum + int(score)  # 然后依次加起来，但分数是字符串，所以要转换    
    result = data[0]+str(sum)+'\n'  # 结果就是学生姓名和总分
    print(result)
    final_scores.append(result)

print(final_scores)

sum1 = open('winner.txt','w+',encoding='utf-8') 
sum1.writelines(final_scores)
sum1.close()