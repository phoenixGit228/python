#%%
"""爬取所有评论"""
import requests, bs4

for x in range(1686,1689):
    url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/comment-page-'
    url = url + str(x) + '/#comments'
    url = url.replace(' ', '')
    print(url)
    res = requests.get(url)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs_comments = bs.find_all(class_='comment-body')
    for comment in bs_comments:
        author = comment.find('b', class_='fn').text
        time = comment.find('time').text.strip()
        ment = comment.find('p').text
        print(author)
        print(time)
        print(ment)
        print()

# %%
"""书店寻宝"""
import requests,bs4
url = "http://books.toscrape.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"} 
res = requests.get(url,headers=headers)
bs = bs4.BeautifulSoup(res.text, 'html.parser')
bs_lists = bs.find(class_='nav nav-list').find('ul').find_all('a')
for catogory in bs_lists:
    print(catogory.text.strip())

# %%
"""所有书的书名、评分、价格三种信息，并且打印提取到的信息"""
import requests, bs4
url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
res = requests.get(url, headers=headers)
bs = bs4.BeautifulSoup(res.text, 'html.parser')
bs_lists = bs.find_all('article')
for result in bs_lists:
    book = result.find('h3').find('a')
    price = result.find(class_='price_color')
    rating = result.find('p')
    print("书名：", book['title'])
    print("评分：", rating['class'][1])
    print("价格：", price.text)
    print()

# %%
