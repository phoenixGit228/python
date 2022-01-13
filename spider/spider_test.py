#%%
"""
爬取网页所有评论
"""

import requests
from bs4 import BeautifulSoup
res = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/')
# print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')
# print(type(soup))
# print(soup)
items = soup.find_all(class_='comment-body')
# print(type(items))
# print(len(items))
# print(items)

for item in items:
    user = item.find(class_='fn')
    time = item.find('time')
    comment = item.find(class_='comment-content')
    # print(type(user))
    # print(type(time))
    # print(type(time.text))
    # print(type(comment.text))
    print(user.text, "\t",time.text.strip(), '\t', comment.text.lstrip())

#%%
"""
爬取分类列表
"""
import requests
from bs4 import BeautifulSoup
res = requests.get('http://books.toscrape.com/catalogue/category/books_1/index.html')
print(res.status_code)
# txt = res.text
# print(txt[1000:2000])
soup = BeautifulSoup(res.text, 'html.parser')
# print(type(soup), '\n')
# print(soup)
items = soup.find('ul',class_='nav nav-list').find_all('li')
print(type(items))
# print(items)
for item in items:
    # print(type(item))

    book_class = item.find('a')
    # print(type(book_class))
    print(book_class.text.strip())

# %%
"""
爬取书名、评级、价格信息
"""
import requests
from bs4 import BeautifulSoup
res = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')
items = soup.find('section').find_all('article')
# print(type(items))
# print(len(items))
# print(items[0])
# print()
for item in items:
    print(type(item))
    print(item)
    # name = item.find(class_='title')
    name = item.find(class_='title')
    print(type(name))
    print()
    # print(name)
    
    # 评级需要修改
    # rate = item.find('p')

    # 价格已获取
    # price = item.find(class_='price_color')
    # print(price.text)

# %%
