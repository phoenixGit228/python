# 获取北京疫情通报信息
import requests
from bs4 import BeautifulSoup


# 用headers模拟浏览器访问网址
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

# 媒体聚焦
print('\n================  媒体聚焦  ===============\n')
for d in range(0, 1):   # range(0-31)
    media_url = 'http://wjw.beijing.gov.cn/wjwh/ztzl/xxgzbd/gzbdmtjj/'
    if d != 0:
        media_url += 'index_' + str(d)+'.html'
    res = requests.get(media_url, headers=headers)  # 1/获取网址
    # print(res.status_code)
    msg = res.text  # 以文本的形式返回值

    msgs = BeautifulSoup(msg, 'html.parser')  # 2/解析获取的数据
    # print(msgs)

    list_msg = msgs.find(class_="bodyTxt").find_all('li', class_='listLk')
    list_time = msgs.find(class_="bodyTxt").find_all('li', class_='listTime')
    # print(list_msg)

    for i in range(len(list_msg)):
        time = list_time[i].text.strip()
        txt = list_msg[i].text.strip()
        # 输出信息
        print(f'{time}\t\t{txt}')

print('\n================  疫情通报  ===============\n')

for d in range(0, 1):   # range(0-31)
    disease_url = 'http://wjw.beijing.gov.cn/wjwh/ztzl/xxgzbd/gzbdyqtb/'
    if d > 0:
        disease_url += 'index_' + str(d)+'.html'
    res = requests.get(disease_url, headers=headers)  # 1/获取网址
    # print(res.status_code)
    msg = res.text  # 以文本的形式返回值

    msgs = BeautifulSoup(msg, 'html.parser')  # 2/解析获取的数据
    # print(msgs)

    list_msg = msgs.find(class_="bodyTxt").find_all('li', class_='listLk')
    list_time = msgs.find(class_="bodyTxt").find_all('li', class_='listTime')
    # print(list_msg)

    for i in range(len(list_msg)):
        time = list_time[i].text.strip()
        txt = list_msg[i].text.strip()
        # 输出信息
        print(f'{time}\t\t{txt}')
