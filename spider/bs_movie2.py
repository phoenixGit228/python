import requests, bs4

# 为躲避反爬机制，伪装成浏览器的请求头
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

num = []
title = []
comment = []
url_movie = []
tes = []

for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x * 25) + '&filter='
    res = requests.get(url, headers=headers)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')

    # 查找序号
    for nums in bs.find_all(class_="pic"):
        num.append(nums.find('em').text)

    # 查找序号、链接
    for hds in bs.find_all('div', class_="hd"):
        title.append(hds.find(class_='title').text)
        url_movie.append(hds.find('a')['href'])

    # 查找推荐语
    for titles in bs.find_all('li'):
        try:
            tes.append(titles.find('span', class_='inq').text)
        except AttributeError:
            tes.append("")

    # 查找评分
    for tag_comment in bs.find_all(class_='star'):
        comment.append(tag_comment.find('span', class_='rating_num').text)

# print(len(tes))        
for i in range(len(num)):
    print(num[i] + '.' + title[i] + '——' + comment[i] + '\n' + '推荐语：' + tes[i] + '\n' + url_movie[i])
