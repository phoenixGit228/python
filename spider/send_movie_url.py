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
movie_name = []
movie_link = []

def movie_spider():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    for x in range(10):
        url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
        res = requests.get(url, headers=headers)
        bs = BeautifulSoup(res.text, 'html.parser')
        bs = bs.find('ol', class_="grid_view")
        for titles in bs.find_all('li'):
            title = titles.find('span', class_="title").text
            movie_list.append(title)
    
def find_movie(movie):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    urlsearch = 'https://www.piaohua.com/plus/search.php'
    params = {
        'kwtype': '0',
        'keyword': movie,
        'searchtype':'影视搜索'
    }
    res = requests.get(urlsearch,headers=headers,params=params)
    res.encoding = 'utf-8'
    bs = BeautifulSoup(res.text, 'html.parser')
    items = bs.find_all(class_='col-md-6')
    if not items:  # 如果返回空列表，表明未找到电影，函数结束
        return 0
    else:
        for item in items:
            name = item.find('h3').find('a')
            movie_name.append(name.text)
            url2 = 'https://www.piaohua.com' + name['href']
            res2 = requests.get(url2, headers=headers)
            res2.encoding = 'utf-8'
            bs2 = BeautifulSoup(res2.text, 'html.parser')
            url3 = bs2.find(class_='txt').find('td').find('a')
            if url3 != None:
                movie_link.append(url3['href'])

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

i = 0
while True:
    movie = movie_list.pop(movie_list.index(random.choice(movie_list)))
    print('电影：', movie)
    download = find_movie(movie)
    if download != 0:
        print('链接：\n', download)
        print()
        i += 1
    else:
        pass

    if i >= 3:
        break
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