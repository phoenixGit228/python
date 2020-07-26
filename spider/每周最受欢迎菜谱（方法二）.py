import requests
from bs4 import BeautifulSoup

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}#用headers模拟浏览器访问网址
res=requests.get('http://www.xiachufang.com/explore/',headers=headers) #1/获取网址
#print(res.status_code)
food=res.text #以文本的形式返回值

week_food=BeautifulSoup(food,'html.parser') #2/解析获取的数据

week_foods=week_food.find_all('p',class_="name")
cailiao = week_food.find_all('p', class_="ing ellipsis")
listfood=[]

for i in range(len(week_foods)):
    list_food=[week_foods[i].text.strip(),'http://www.xiachufang.com/explore/'+week_foods[i].find('a')['href'],cailiao[i].text.strip()]
    listfood.append(list_food)
print(listfood)
