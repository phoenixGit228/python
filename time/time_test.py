# %%
import time

localtime1 = time.time()
# print(localtime1)
# localtime1 = time.localtime(time.time())
# print(localtime1)
# localtime1 = time.mktime(localtime1)
# print(localtime1)
# localtime1 = time.localtime(localtime1)
# print(localtime1)
# print('=================')
# localtime1 = time.time()
# print(localtime1)
# localtime1 = time.gmtime(localtime1)
# print(localtime1)
# localtime1 = time.mktime(localtime1) #local时间，不是gmtime！
# print(localtime1)
localtime1 = time.localtime(localtime1)
print(localtime1)

localtime2 = time.strftime("%a |  %A  ",localtime1) # 星期简写/全称
print(localtime2)

localtime2 = time.strftime("%b | %B ",localtime1) # 月英文简写/全称
print(localtime2)
localtime2 = time.strftime(" %c | %d ",localtime1) # 本地日期(星期，月，日，时间，年) / 日
print(localtime2)
localtime2 = time.strftime(" %H | %I | %j | %m ",localtime1) #本地时、分、年中日？、数字月
print(localtime2)
localtime2 = time.strftime(" %p | %S | %U  | %W",localtime1) #PM/AM、秒、一年中的周数（星期日作为开始）、一年中的周数（星期一作为开始）
print(localtime2)
localtime2 = time.strftime(" %x | %X ",localtime1) # 月日年、时分秒
print(localtime2)
localtime2 = time.strftime(" %y | %Y ",localtime1) # 年简写、全称
print(localtime2)
localtime2 = time.strftime(" %z | %Z",localtime1) 
print(localtime2)

#%%
# 倒计时显示功能：

import time
for i in range(20,0,-1):
    print("\r倒计时{}秒！".format(i),end="")
    time.sleep(1)
print("\r倒计时结束！")

# %% 转圈显示功能
import time
sum = 10        #设置倒计时时间
interval = 0.25 #设置屏幕刷新的间隔时间
for i in range(0,int(sum/interval)):
    list=["\\","|","/","-"]
    index = i%4
    print("\r程序正在运行 {}".format(list[index]),end="")
    time.sleep(interval)


# %% 进度条显示功能
import time
sum = 50         #设置倒计时时间
interval = 0.5   #设置屏幕刷新的间隔时间
for i in range(0,int(sum/interval)+1):
    print("\r正在加载:" + "|" +"*"*i + " "*(int(sum/interval)+1-i)+"|" +str(i)+"%",end="")
    time.sleep(interval)
print("\r加载完成！")

# %%
import time
 
# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 
# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())) 
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
print(time.mktime(time.strftime(a,"%a%Y%d%H%M%S")))
# %%
import time

with open ('')