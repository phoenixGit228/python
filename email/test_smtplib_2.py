# 读取CSV
import csv
# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
from email.header import Header


to_addrs = [['kaixi', 'kaixi@qq.com'], ['wanzi', 'wanzi@qq.com']]
for i in to_addrs:
    print(i[1])
with open('to_addrs.csv', 'w', encoding='utf-8') as f:
    for i in to_addrs:
        f.writerow(i)

with open('to_addrs.csv', 'r', encoding='utf-8') as f:
    fwrite = f.readlines()
    print(type(fwrite))
    print(fwrite)

# email 用于构建邮件内容

# 发信方的信息：发信邮箱，QQ 邮箱授权码
# from_addr = '147306542@qq.com'
from_addr = input('请输入发件人邮箱：')
# password = 'obgiuvkyvcypbhfg'
password = input('请输入用户密码：')
# 收信方邮箱
# to_addr = ['147306542@qq.com','phoenix228@qq.com']
to_addr = []
while True:
    new_addr = input("请输入收件人邮箱：")
    to_addr.append(new_addr)
    b = input("请输入是否继续输入收件人地址：n-否，")
    if b == 'n':
        break

to_addrs = ','.join(to_addr)
print(to_addrs)

# 发信服务器
smtp_server = 'smtp.qq.com'
text = '''亲爱的学员，你好！
​    我是吴枫老师，能遇见你很开心。
​    希望学习Python对你不是一件困难的事情！

人生苦短，我用Python
'''
# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
msg = MIMEText(text, 'plain', 'utf-8')
# msg['From'] = Header(from_addr,'utf-8')
# msg['To'] = Header(to_addr, 'utf-8')
# subject = 'Python 邮件测试'
# msg['Subject'] = Header(subject,'utf-8')

msg['From'] = Header('phoenix228')
msg['To'] = Header('147306542')
msg['Subject'] = Header('python test')


# 开启发信服务，这里使用的是加密传输
# server = smtplib.SMTP()
# server.connect(smtp_server, 25)
try:
    server = smtplib.SMTP_SSL(smtp_server)
    server.connect(smtp_server,465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()
except smtplib.SMTPException:
    print('无法发送邮件')
    