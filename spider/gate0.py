# %%
"""下载文件"""
import requests
url = "ht t ps://localprod.pandat eacher.com/pyt hon-manuscript /crawler-ht ml/exercise/HT T P响应状态码.md"
url = url.replace(' ', '')
res = requests.get(url)
print(res.status_code)
with open('HTTP响应状态码.md', 'w+') as file1:
    file1.write(res.text)
    print('下载完成')

# %%
"""download image"""
url = "ht t ps://res.pandat eacher.com/2019-01-12-15-29-33.png"
url = url.replace(' ', '')
res = requests.get(url)
print(res.headers)
with open('pic.png', 'wb', buffering=200) as pic:  # 流文件的open不带编码
    pic.write(res.content)

# %%
"""下载音频文件"""
url = "https://static.pandateacher.com/Over%20The%20Rainbow.mp3"
r = requests.get(url)
with open('Ranbow.mp3', 'wb', buffering=100) as file1:
    file1.write(r.content)

# %%
res = requests.get(
    'https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
print(res.status_code)
res.encoding = 'utf-8'
download = res.text
daima = open('这个书苑不太冷5.0的网页源代码.txt', 'a+', encoding='utf-8')
daima.write(download)
daima.close()

# %%
import requests
url = 'http://192.168.3.19/'
res = requests.get(url)
print(res.status_code)
# %%
