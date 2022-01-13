import csv
import time
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
data_file = input('请输入所要加载数据路径:\n')
with open(data_file, 'r', encoding='gbk') as f:
    reader = csv.reader(f)
    # 读取csv文件
    reader_list = list(reader)
    print(len(reader_list))
    # 读取的文件转为list
    tag = reader_list[0]
    print(len(tag))
    n = 0
    # 保存csv首行位号
    for i in range(1, len(reader_list)):
        for j in range(len(tag)):
            try:
                r.set(tag[j], float(reader_list[i][j]))
            except:
                pass
        print(r.get('CYC::KCATW71'))
        time.sleep(1)
        n += 1
print(n)
