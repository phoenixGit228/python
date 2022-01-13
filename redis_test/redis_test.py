# 导入csv模块
import csv
# 导入redis模块
import redis
# 导入time模块
import time

# 连接redis数据库
r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

with open('data.csv', 'r', encoding='gbk') as f:
    rows = csv.DictReader(f)
    print(rows)
    n = 1
    for row in rows:
        for key, value in row.items():
            try:
                r.set(key, float(value))  # 将内容写入redis
            except ValueError:
                pass
        print(f"数据写入完成至第{n}行")
        n += 1
        time.sleep(1)
print('数据写入完毕')