"""薄荷网，获取食物卡路里"""
from gevent import monkey
monkey.patch_all()
import gevent, csv, requests,time
from bs4 import BeautifulSoup
from gevent.queue import Queue
start = time.time()
work = Queue()
for x in range(1, 11):
    for y in range(1,11):
        url = f'http://www.boohee.com/food/group/{x}?page={y}'
        # url = 'http://www.boohee.com/food/group/{}?page={}'.format(x,y)
        work.put_nowait(url)

for x in range(1, 11):
    work.put_nowait(f'http://www.boohee.com/food/view_menu?page={x}')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
csv_file = open('foods_energy3.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
writer.writerow(['分类','食物','热量','链接'])
def spider():
    while not work.empty():
        url = work.get_nowait()
        r = requests.get(url, headers=headers)
        r.encoding = 'utf-8'
        bs = BeautifulSoup(r.text, 'html.parser')
        catagory = bs.find(class_='widget-food-list pull-right').find('h3').text.strip()
        foods = bs.find_all(class_='text-box pull-left')
        for food in foods:
            title = food.find('a').text
            link = food.find('a')['href']
            link = 'http://www.boohee.com' + link
            energy = food.find('p').text.replace('热量：','')
            writer.writerow([catagory, title, energy, link])

job_list = []

for x in range(5):
    job = gevent.spawn(spider)
    job_list.append(job)

gevent.joinall(job_list)
csv_file.close()
end = time.time()
print('资料搜集完毕！')
print(end - start)