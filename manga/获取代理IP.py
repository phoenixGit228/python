import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome() # 设置引擎为Chrome，真实地打开一个Chrome浏览器
driver.get('http://www.goubanjia.com/')

time.sleep(2)
items = driver.find(class_='container-fluid').find('tbody').find_all('tr')
for item in items:
    ip = item.find(class_='ip').text
    http = item.find(title='https代理IP').text
    print(f"ip: {ip}, http: {http}")

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

# url = "http://www.goubanjia.com/"

# res = requests.get(url, headers=headers)
# if res.status_code == 200:
#     # print(res.text)
#     bs = BeautifulSoup(res.text, "html.parser")
#     items = bs.find(class_='container-fluid').find('tbody').find_all('tr')
#     for item in items:
#         ip = item.find(class_='ip').text
#         http = item.find(title='https代理IP').text
#         print(f"ip: {ip}, http: {http}")
