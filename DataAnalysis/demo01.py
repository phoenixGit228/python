import pymysql

# 打开
conn = pymysql.connect(host="rm-2ze0u172x2a69w5h6qo.mysql.rds.aliyuncs.com",
                       port=3306,
                       user="aura",
                       password="zgbLZTgs",
                       database="aura",
                       charset="utf8mb4")

cursor = conn.cursor(pymysql.cursors.DictCursor)

# 操作

# sql = "SELECT COUNT(*) AS `学生总数` FROM student;"

sql = """
SELECT 
    class AS `班级`,
    MAX(english) AS `英语最高分`,
    MIN(math) AS `数学最低分`,
    AVG(chinese) AS `汉语平均分`, 
    SUM(english + math + chinese) AS `总分`
FROM 
    student 
WHERE
	math IS NOT NULL 
	AND english IS NOT NULL 
	AND chinese IS NOT NULL

	AND math BETWEEN 0 AND 100
	AND english BETWEEN 0 AND 100
	AND chinese BETWEEN 0 AND 100
GROUP BY class;
"""
nums = cursor.execute(sql)
data = cursor.fetchall()
for item in data:
    print(item)

# 关闭

cursor.close()
conn.close()
