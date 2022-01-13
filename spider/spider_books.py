"""
爬取书名、评级、价格信息
"""
import requests
from bs4 import BeautifulSoup

res = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
# print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')
#找到标签后, 这里需要嵌套提取好几层, 这样的定位会比较准确
#find('ul',class_='nav nav-list').find('ul').find_all('li')
items = soup.find('section').find_all('article')

def star(x):
    rating = ['one', 'two', 'three', 'four', 'five']
    star_num = ["★","★ ★","★ ★ ★","★ ★ ★ ★","★ ★ ★ ★ ★"]
    return star_num[rating.index(x.lower())]

for item in items:
    # 书名
    name = item.find('img')
    print("书名：", name['alt'])  
    # 评级
    rate = item.find('p',class_='star-rating')
    # 由于’class‘属性的名字字符串'star-rating two/Three'带有空格，
    # 因此获取的属性会分割成两个字符串组成的列表
    print("评级：", star(rate['class'][1]))
    print("评级：", rate['class'][1])   
    # 价格
    price = item.find(class_='price_color')
    print("价格：", price.text)
    # 存货
    stock = item.find(class_='instock availability')
    print("状态：", stock.text.strip())
    print()