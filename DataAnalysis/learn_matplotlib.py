""" matplotlib 绘图"""
import random
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['simHei'] # 显示中文
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号
fig = plt.figure(figsize=(10,8),dpi=80)

# 创建列表
x = range(120)
y = [random.randint(20,35) for i in range(120)]
# 设置标签
plt.xlabel(u'序列1')
plt.ylabel(u'序列2')
plt.xticks(x[::10])
# plt.yticks(range(min(y),max(y)+1))
# 绘图
plt.plot(x,y)
# 保存图形
plt.savefig('./figure01.png')
# 展示图形
plt.show()