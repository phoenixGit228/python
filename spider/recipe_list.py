#%%
import requests
from bs4 import BeautifulSoup

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Connection': 'keep-alive',
    'Referer': 'http://www.baidu.com/'
}

website = 'http://www.xiachufang.com/explore/'
res = requests.get(website,headers = headers)
print(res.status_code)
print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
items = soup.find_all('div', class_='info pure-u')
print(type(items))
print(items)
for item in items:
    recipe = item.find(class_='name')
    sub_url = recipe['href']
    url = website + sub_url[1:]
    ellipsis = item.find('p', class_='ing ellipsis')
    print(recipe.text, url, ellipsis.text.strip())


#%%
# 引用requests库
import requests
# 引用BeautifulSoup库
from bs4 import BeautifulSoup

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

# 创建一个空列表，用于存储信息
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
    print(name,'\n',URL,'\n',ingredients,'\n')
    list_all.append([name,URL,ingredients])

# 打印
# print(list_all)

# %%
"""
打印菜谱的另一种思路
"""
# 引用requests库
import requests
# 引用BeautifulSoup库
from bs4 import BeautifulSoup

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
tags = bs_foods.find_all('p', class_='name')
foods = bs_foods.find_all('p', class_='ing ellipsis')

list_all = []

# print(list_all)

for i in range(len(tags)):
    name = tags[i].find('a')
    list_food=[name.text.strip(),'http://www.xiachufang.com'+name['href'],foods[i].text.strip()]
    list_all.append(list_food)

# 输出所有
# print(list_all)
# 打印各个菜单
for i in range(len(list_all)):
    for j in range(len(list_all[i])):
        print(list_all[i][j])
    print()



# %%
import requests, bs4

# 为躲避反爬机制，伪装成浏览器的请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url, headers=headers)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em',class_="").text
        #查找序号
        # title = titles.find('span', class_="title").text
        title = titles.find('div',class_='hd').find('a').text
        #查找电影名
        tes = titles.find('span', class_='inq').text.replace(" ", "")
        #查找推荐语
        comment = titles.find('span',class_="rating_num").text
        #查找评分
        url_movie = titles.find('a')['href']

        print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes + '\n' + url_movie)
        

# %%
# 引用requests库
import requests
# 引用BeautifulSoup库
from bs4 import BeautifulSoup

# 获取数据
res_foods = requests.get('http://www.xiachufang.com/explore/')
# 解析数据
bs_foods = BeautifulSoup(res_foods.text,'html.parser')

# 查找包含菜名和URL的<p>标签
tag_name = bs_foods.find_all('p',class_='name')
# 查找包含食材的<p>标签
tag_ingredients = bs_foods.find_all('p',class_='ing ellipsis')
# 创建一个空列表，用于存储信息
list_all = []
# 启动一个循环，次数等于菜名的数量
for x in range(len(tag_name)):
    # 提取信息，封装为列表。此处[18:-14]切片的主要功能是切掉空格
    list_food = [tag_name[x].text[18:-14],tag_name[x].find('a')['href'],tag_ingredients[x].text[1:-1]]
    # 将信息添加进list_all
    list_all.append(list_food)

# 打印
print(list_all)

#%%
# 以下是另外一种解法

# 查找最小父级标签
list_foods = bs_foods.find_all('div',class_='info pure-u')
# 创建一个空列表，用于存储信息
list_all = []

for food in list_foods:
    # 提取第0个父级标签中的<a>标签
    tag_a = food.find('a')
    # 菜名，使用[17:-13]切掉了多余的信息
    name = tag_a.text[17:-13]
    # 获取URL
    URL = 'http://www.xiachufang.com'+tag_a['href']
    # 提取第0个父级标签中的<p>标签
    tag_p = food.find('p',class_='ing ellipsis')
    # 食材，使用[1:-1]切掉了多余的信息
    ingredients = tag_p.text[1:-1]
    # 将菜名、URL、食材，封装为列表，添加进list_all
    list_all.append([name,URL,ingredients])

# 打印
print(list_all)