import requests
from bs4 import BeautifulSoup
from urllib.request import quote
#quote()函数，可以帮我们把内容转为标准的url格式，作为网址的一部分打开
# a = '无名之辈'
# print(quote(a.encode('gbk')))
movie_name = input("请输入需要搜索的电影名字:")
gbkmovie = movie_name.encode('gbk')
# 固定的搜索地址
# http: // s.ygdy8.com / plus / s0.php?typeid=1&keyword=
url = "http://s.ygdy8.com/plus/s0.php?typeid=1&keyword=" + quote(gbkmovie)
res = requests.get(url)
#下载××电影的搜索页面
res.encoding ='gbk'
# 为躲避反爬机制，伪装成浏览器的请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
search = requests.get(url, headers=headers)
bs = BeautifulSoup(search.text, 'html.parser')
movies = bs.find('div', class_='co_content8').find('ul').find('b').find('a')

movie_page = 'https://www.ygdy8.com/' + movies['href']

search_page = requests.get(movie_page, headers=headers)

search_page.encoding='gbk'

bs1 = BeautifulSoup(search_page.text, 'html.parser')

down_link = bs1.find('div',id="Zoom").find('span').find('table').find('a')

print("迅雷链接：\n", down_link['href'])