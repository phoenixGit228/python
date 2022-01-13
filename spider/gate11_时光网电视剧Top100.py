# %%
"""
项目目标：
使用多协程和队列，爬取时光网电视剧TOP100的数据（剧名、导演、主演和简介），并用csv模块将数据存储下来。"""

from gevent import monkey
monkey.patch_all()
import gevent, requests, bs4, csv,time
from gevent.queue import Queue

start = time.time()
work = Queue()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
url = 'http://www.mtime.com/top/tv/top100/'
url_list = [url]
for i in range(2, 11):
    url_list.append(url + 'index-' + str(i) + '.html')

for urls in url_list:
    work.put_nowait(urls)

file1 = open('top100.csv', 'w', encoding='utf-8',newline='')
writer = csv.writer(file1)
writer.writerow(['评级','名称','导演','主演','电影简介'])
def crawler():
    while not work.empty():
        url = work.get_nowait()
        r = requests.get(url, headers=headers)
        r.encoding = 'utf-8'
        bs = bs4.BeautifulSoup(r.text, 'html.parser')
        dramas = bs.find(id='asyncRatingRegion').find_all('li')
        list1 = []
        for drama in dramas:
            rating = drama.find(class_='number').text
            name = drama.find('div',class_='mov_con').find('h2').text
            content = drama.find('div',class_='mov_con').find_all('p')
            men = ['','','']
            for info in content:
                if '导演' in info.text:
                    men[0] = info.text
                elif '主演' in info.text:
                    men[1] = info.text
                else:
                    men[2] = info.text
            list1.append([rating, name]+ men)

        for txt in list1:
            writer.writerow(txt)

task_list = []
for x in range(2):
    task = gevent.spawn(crawler)
    task_list.append(task)
gevent.joinall(task_list)

file1.close()
end = time.time()
print(end - start)

