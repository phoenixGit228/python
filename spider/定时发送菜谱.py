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

        list_all.append('{}\n链接：{}\n配料：{}'.format(name,URL,ingredients))
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

schedule.every().day.at("11:56").do(job) 
while True:
    schedule.run_pending()
    time.sleep(1)
