import csv
import redis
r = redis.StrictRedis(host='127.0.0.1', port=6379, db=1, password='123456')

with open('data.csv', 'r', encoding='gbk') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        name = row['Time']
        id = row['PDI2104.PV']
        print(row)
        r.set(name,id)  #将内容写入redis
