import requests
from bs4 import BeautifulSoup

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options  # 从options模块中调用Options类

chrome_options = Options() # 实例化Option对象
# chrome_options.add_argument('--headless') # 对浏览器的设置
driver = webdriver.Chrome()
url = 'http://www.dianping.com/renqiu/ch10'
headers = {
    # 'Host': 'mlog.dianping.com',
    # 'Origin': 'https://www.dianping.com',
    # 'Referer': 'https://www.dianping.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

driver.get(url) # 访问页面
time.sleep(2) # 等待2秒
label = driver.find_element(By_Class,'con')  # 解析网页并提取第一个<label>标签
print(label.text) # 打印label的文本
items = label.find_elements_by_tag_name('a')

# for item in items:
#     catagory = item.text
#     url = item['href']
#     print(catagory, url)
# driver.close()  # 关闭浏览器


