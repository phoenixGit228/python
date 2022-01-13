#%%
"""
下载图片
""" 
import requests
res = requests.get("https://res.pandateacher.com/2018-12-18-10-43-07.png")
pic = res.content
with open("ppt.png", "wb") as file1:
    file1.write(pic)

#%%
"""
下载《三国演义》章节回目
"""
# 引用requests库
import requests

# 下载《三国演义》第一回，我们得到一个对象，它被命名为res
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
# 把Response对象的内容以字符串的形式返回
novel=res.text
# 现在，可以打印小说了，但考虑到整章太长，只输出800字看看就好。在关于列表的知识那里，你学过[:800]的用法。
print(novel[:800])

# %%
"""
下载《三国演义》章节回目
"""
# 引入requests库
import requests
#下载《三国演义》第一回，我们得到一个对象，它被命名为res
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
# 把Response对象的内容以字符串的形式返回
novel = res.text
# 创建一个名为《三国演义》的txt文档，指针放在文件末尾，追加内容
k = open('《三国演义》.md','a+',encoding=res.encoding)
# k = open('《三国演义》.md','a+')
# 写进文件中 
k.write(novel)
# 关闭文档    
k.close()


# %%
"""
爬取robots协议
"""
import requests
res = requests.get('http://www.taobao.com/robots.txt')
txt = res.text
with open('robots.txt', 'w+') as rob:
    rob.write(txt)


# %%
"""
保存文件
"""
import requests
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md')
code = res.encoding
txt = res.text
with open('HTTP状态相应码.md','w', encoding=code) as file:
    file.write(txt)
    

# %%
"""
保存图片
"""
import requests
res = requests.get('https://res.pandateacher.com/2019-01-12-15-29-33.png')

with open('spider.png', 'wb') as pic:
    pic.write(res.content)

# %%
"""
保存网页mp3
"""
import requests
url = "https://static.pandateacher.com/Over%20The%20Rainbow.mp3"
res = requests.get(url)

with open('rainbow.mp3', 'wb') as music:
    music.write(res.content)

# %%
"""
爬取网页
"""

import requests
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
with open('test.html','w',encoding=res.encoding) as htm:
    htm.write(res.text)

# %%
"""
学习BeautifulSoup模块
"""
import requests
from bs4 import BeautifulSoup
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
soup = BeautifulSoup(res.text, 'html.parser')
items = soup.find_all(class_='books')
for item in items:
    kind = item.find('h2')
    title = item.find(class_='title')
    info = item.find(class_='info')
    print(kind, '\n', title, '\n', info, '\n')
    print(kind.text, '\n', title.text,'\n',title['href'], '\n',info.text,'\n')
    # print(type(item))
    # print(item)

# %%
