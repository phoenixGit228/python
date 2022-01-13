# 导入redis模块
import redis
# 导入time模块
# import time

# 连接redis数据库
# r = redis.StrictRedis(host='127.0.0.1', port=6379,db=0, decode_responses=True)
pool = redis.ConnectionPool(host='127.0.0.1', port=6379,db=0)
r = redis.Redis(connection_pool=pool)

# print(type(r.zrange('tag:2,KPIHOIL',0, -1)))
# print(r.zrange('tag:2,1020-AI1001',0, -1))
line = r.zrange('tag:2,KPIHOIL_PV',0, -1)
print(line)
data = []
for i in range(0, len(line)):
    s = line[i].decode('utf-8').split(';')[1]
    data.append(s)
print(data)
# print(type(line[0]))
# print(line[0])
# s = line[0].decode('utf-8')

# print(type(s))
# print(s)
# print(s.split(';')[1])
