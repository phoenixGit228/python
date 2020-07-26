"""
爬取文章、链接、日期
"""
import requests
from bs4 import BeautifulSoup
res = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/')
# print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')
items = soup.find_all('article')
# print(type(items))
for item in items:
    title = item.find('h2')
    # 不找到最小标签，不能直接使用属性
    link = title.find('a')
    date = item.find('time')
    print(title.text, '\n',
          link['href'],'\n',
          date.text, '\n')