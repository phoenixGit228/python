#%%
"""爬取天气预报"""
import requests
from bs4 import BeautifulSoup
#引入requests库和BeautifulSoup库
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
#封装headers
url='http://www.weather.com.cn/weather/101280601.shtml'
#把URL链接赋值到变量url上。
res=requests.get(url,headers=headers)
#发送requests请求，并把响应的内容赋值到变量res中。
print(res.status_code)
#检查响应状态是否正常
res.encoding='utf-8'
print(res.text)
#打印出res对象的网页源代码   

#%%
"""发送邮件"""
import smtplib 
from email.mime.text import MIMEText
from email.header import Header
#引入smtplib、MIMEText和Header

mailhost='smtp.qq.com'
#把qq邮箱的服务器地址赋值到变量mailhost上，地址应为字符串格式
qqmail = smtplib.SMTP()
#实例化一个smtplib模块里的SMTP类的对象，这样就可以调用SMTP对象的方法和属性了
qqmail.connect(mailhost,25)
#连接服务器，第一个参数是服务器地址，第二个参数是SMTP端口号。
#以上，皆为连接服务器。

account = input('请输入你的邮箱：')
#获取邮箱账号，为字符串格式
password = input('请输入你的密码：')
#获取邮箱密码，为字符串格式
qqmail.login(account,password)
#登录邮箱，第一个参数为邮箱账号，第二个参数为邮箱密码
#以上，皆为登录邮箱。

receiver=input('请输入收件人的邮箱：')
#获取收件人的邮箱。

content=input('请输入邮件正文：')
#输入你的邮件正文，为字符串格式
message = MIMEText(content, 'plain', 'utf-8')
#实例化一个MIMEText邮件对象，该对象需要写进三个参数，分别是邮件正文，文本格式和编码
subject = input('请输入你的邮件主题：')
#输入你的邮件主题，为字符串格式
message['Subject'] = Header(subject, 'utf-8')
#在等号的右边是实例化了一个Header邮件头对象，该对象需要写入两个参数，分别是邮件主题和编码，然后赋值给等号左边的变量message['Subject']。
#以上，为填写主题和正文。

try:
    qqmail.sendmail(account, receiver, message.as_string())
    print ('邮件发送成功')
except:
    print ('邮件发送失败')
qqmail.quit()
#以上为发送邮件和退出邮箱。

#%%
"""shedule模块，实现定时功能"""
import schedule
import time
#引入schedule和time

def job():
    print("I'm working...")
#定义一个叫job的函数，函数的功能是打印'I'm working...'

schedule.every(10).minutes.do(job)       #部署每10分钟执行一次job()函数的任务
schedule.every().hour.do(job)            #部署每×小时执行一次job()函数的任务
schedule.every().day.at("10:30").do(job) #部署在每天的10:30执行job()函数的任务
schedule.every().monday.do(job)          #部署每个星期一执行job()函数的任务
schedule.every().wednesday.at("13:15").do(job)#部署每周三的13：15执行函数的任务

while True:
    schedule.run_pending()
    time.sleep(1)    
#15-17都是检查部署的情况，如果任务准备就绪，就开始执行任务。   

#%%
"""schedule 模块"""
import schedule
import time
#引入schedule和time模块
def job():
    print("I'm working...")
#定义一个叫job的函数，函数的功能是打印'I'm working...'
schedule.every(2).seconds.do(job)        #每2s执行一次job()函数

while True:
    schedule.run_pending()
    time.sleep(1)


#%%
"""定时发送天气预报"""
import requests
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

account = input('请输入你的邮箱：')
password = input('请输入你的密码：')
receiver = input('请输入收件人的邮箱：')

def weather_spider():
    headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url='http://www.weather.com.cn/weather/101280601.shtml'
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    tem1= soup.find(class_='tem')
    weather1= soup.find(class_='wea')
    tem=tem1.text
    weather=weather1.text
    return tem,weather

def send_email(tem,weather):
    mailhost='smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)
    qqmail.login(account,password)
    content= tem+weather
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '今日天气预报'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()

def job():
    print('开始一次任务')
    tem,weather = weather_spider()
    send_email(tem,weather)
    print('任务完成')

schedule.every().day.at("07:30").do(job) 
while True:
    schedule.run_pending()
    time.sleep(1)

#%%
"""定时发送菜谱"""
import requests
from bs4 import BeautifulSoup
#引入smtplib、MIMEText和Header
import smtplib 
from email.mime.text import MIMEText
from email.header import Header
import schedule
import time

account = input('请输入你的邮箱：')
password = input('请输入你的密码：')
receiver = input('请输入收件人的邮箱：')

def menu():
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
        'Connection': 'keep-alive',
        'Referer': 'http://www.baidu.com/'
    }

    # 获取数据
    res_foods = requests.get('http://www.xiachufang.com/explore/',headers=headers)
    # 解析数据
    bs_foods = BeautifulSoup(res_foods.text,'html.parser')
    # 查找最小父级标签
    list_foods = bs_foods.find_all('div',class_='info pure-u')
    list_all = []
    for food in list_foods:
        tag_a = food.find('a')
        # 菜名，使用strip()函数去掉多余的空格
        name = tag_a.text.strip()
        # 获取URL
        URL = 'http://www.xiachufang.com'+tag_a['href']
        tag_p = food.find('p',class_='ing ellipsis')
        # 食材，使用strip()函数去掉多余的空格
        ingredients = tag_p.text.strip()
        # 将菜名、URL、食材，封装为列表，添加进list_all
        # print(name,'\n',URL,'\n',ingredients,'\n')
        list_all.append(name+'\n'+URL+'\n'+ingredients+'\n')
        # list_all.append('{}\n链接：{}\n配料：{}'.format(name,URL,ingredients))
    return '\n\n'.join(list_all)

def send_email(recipe):
    mailhost='smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)
    qqmail.login(account,password)
    content= recipe
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '本周推荐菜谱'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()

def job():
    print('开始一次任务')
    recipe = menu()
    send_email(recipe)
    print('任务完成')

schedule.every(1).minutes.do(job) 
# schedule.every().day.at("15:03").do(job) 
while True:
    schedule.run_pending()
    time.sleep(1)


# %%
"""这是爬取豆瓣电影Top250，并存为本地csv的代码"""

import requests, random, csv, smtplib, schedule, time
from bs4 import BeautifulSoup
from urllib.request import quote
from email.mime.text import MIMEText
from email.header import Header
#引入smtplib、MIMEText和Header

# account = input('请输入你的邮箱：')
# #获取邮箱账号，为字符串格式
# password = input('请输入你的密码：')
# #获取邮箱密码，为字符串格式
# receiver=input('请输入收件人的邮箱：')
movie_list = []
movie_link = []
def movie_spider():
    # csv_file=open('movieTop.csv', 'w', newline='',encoding='utf-8')
    # writer = csv.writer(csv_file)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    for x in range(10):
        url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
        res = requests.get(url, headers=headers)
        bs = BeautifulSoup(res.text, 'html.parser')
        bs = bs.find('ol', class_="grid_view")
        for titles in bs.find_all('li'):
            title = titles.find('span', class_="title").text
            movie_list.append(title)
            # writer.writerow(list1)
    # csv_file.close()
    
def find_movie():
    # movie=input('你想看什么电影？')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    for movie in movies:
        # gbkmovie = movie.encode('gbk')
        print(movie)
        urlsearch = 'https://www.piaohua.com/plus/search.php'
        params = {
            'kwtype': '0',
            'keyword': movie,
            'searchtype':'影视搜索'
        }
        res = requests.get(urlsearch,headers=headers,params=params)
        # res.encoding = 'gbk'
        print(res.status_code)
        print(res.encoding)
        # bs = BeautifulSoup(res.text, 'html.parser')
        # url2 = bs.find('ul').find('a')
        # url2 = 'https://www.ygdy8.com/' + url2['href']
        # res2 = requests.get(url2, headers=headers)
        # bs2 = BeautifulSoup(res2.text, 'html.parser')
        # thunder = bs2.find(id='zoom').find('a')
        # movie_link.append(movie +' '+ thunder['xbmwzzdk'])

def send_mail(content):
    mailhost='smtp.qq.com'
    #把qq邮箱的服务器地址赋值到变量mailhost上，地址应为字符串格式
    qqmail = smtplib.SMTP()
    #实例化一个smtplib模块里的SMTP类的对象，这样就可以调用SMTP对象的方法和属性了
    qqmail.connect(mailhost,25)
    #连接服务器，第一个参数是服务器地址，第二个参数是SMTP端口号。
    #以上，皆为连接服务器。

    #获取收件人的邮箱。
    qqmail.login(account,password)
    #登录邮箱，第一个参数为邮箱账号，第二个参数为邮箱密码

    #content为上面的电影链接
    #输入你的邮件正文，为字符串格式
    message = MIMEText(content, 'plain', 'utf-8')
    #实例化一个MIMEText邮件对象，该对象需要写进三个参数，分别是邮件正文，文本格式和编码
    subject = '电影链接'
    #输入你的邮件主题，为字符串格式
    message['Subject'] = Header(subject, 'utf-8')
    #在等号的右边是实例化了一个Header邮件头对象，该对象需要写入两个参数，分别是邮件主题和编码，然后赋值给等号左边的变量message['Subject']。
    #以上，为填写主题和正文。

    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()
    #以上为发送邮件和退出邮箱

#定时功能是第10关教的内容，代码如下，下面提供代码给大家，但最好回忆不起来再看。

movie_spider()
# print(movie_list)
movies = random.sample(movie_list, 3)
print(movies)
find_movie()
# print(movie_link)
# def job():
#     movies = random.sample(movie_list, 3)
#     find_movies(movies)
#     content = '\n\n'.join(movie_link)
#     send_mail(content)
#     # print("I'm working...")
# #定义一个叫job的函数，函数的功能是打印'I'm working...'

# schedule.every(1).minutes.do(job)       #部署每10分钟执行一次job()函数的任务
# schedule.every().hour.do(job)            #部署每×小时执行一次job()函数的任务
# schedule.every().day.at("10:30").do(job) #部署在每天的10:30执行job()函数的任务
# schedule.every().monday.do(job)          #部署每个星期一执行job()函数的任务
# schedule.every().wednesday.at("13:15").do(job)#部署每周三的13：15执行函数的任务

# while True:
#     schedule.run_pending()
#     time.sleep(1)

# %%
