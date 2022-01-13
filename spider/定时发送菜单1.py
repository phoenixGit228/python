import requests          #导入requests库
import smtplib           #发送邮件使用
import schedule         #定时发送
import time             #时间模块
from bs4 import BeautifulSoup          #导入BeautifulSoup
from email.mime.text import MIMEText        #构建邮件内容 
from email.header import Header          #构建邮件头

#输入隐私信息
mailbox = input('请输入你的邮箱：')
password = input('请输入你的密码：')
receiver = input('请输入收件人的邮箱')

#爬取数据
def foods():
    url = 'http://www.xiachufang.com/explore/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    res = requests.get(url,headers = headers)
    soup = BeautifulSoup(res.text,'html.parser')
    list_foods = soup.find_all('div',class_ = 'info pure-u')
    
    list_all = []
    
    for food in list_foods:
        title = food.find('a').text.strip()
        herf = 'http://www.xiachufang.com' + food.find('a')['href']
        pei_l = food.find('p',class_ = 'ing ellipsis').text.strip()
        # list_all.append([title,herf,pei_l])
        # format方法
        # list_all.append('{}\n链接：{}\n配料：{}'.format(title,herf,pei_l))
        # f-string方法
        list_all.append(f'{title}\n链接：{herf}\n配料：{pei_l}')
    # return list_all
    return ' \n\n'.join(list_all)

#发送邮件
def send_email(list_all):
    global mailbox,password,receiver         #设置为全局变量
    mailhost = 'smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)
    qqmail.login(mailbox,password)
    content = list_all
    message = MIMEText(content,'plain','utf-8')
    subject = '本周最受欢迎菜谱'
    message['subject'] = Header(subject,'utf-8')
    try:
        qqmail.sendmail(mailbox,receiver,message.as_string())
        print('邮件发送成功')
    except:
        print('邮件发送失败')
    qqmail.quit()

#定时执行任务
def job():
    print('开始执行')
    list_all = foods()       #调取爬取数据的函数并将结果赋值给新变量
    print(type(list_all))
    print(list_all)
    send_email(list_all)     #调取发送邮件的函数，并传入邮件内容
    print('任务完成')
job()    
# schedule.every().day.at("16:13").do(job)        #设定每天10:30执行任务
# while True:         #当符合条件的情况下就执行任务
#     schedule.run_pending()
#     time.sleep(2)
