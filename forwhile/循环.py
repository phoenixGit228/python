# i = 0
# while i<5:
#     print('明日复明日')
#     i = i+1
#     print('此时i =',i)
#     if i==3:  # 当i等于3的时候触发
#         break # 结束循环
#     print('此时i= ',i, '\n')
    
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
print(dir(MIMEText))
print(MIMEImage)
print(MIMEMultipart)