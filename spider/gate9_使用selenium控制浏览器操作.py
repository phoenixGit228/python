#%%
# 本地环境的浏览器设置
from selenium import webdriver #从selenium库中调用webdriver模块
import time

driver = webdriver.Chrome() # 设置引擎为Chrome，真实地打开一个Chrome浏览器
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') 
time.sleep(2)

teacher = driver.find_element_by_id('teacher')
teacher.send_keys('必须是吴枫呀')
assistant = driver.find_element_by_name('assistant')
assistant.send_keys('都喜欢')
time.sleep(1)
button = driver.find_element_by_class_name('sub')
time.sleep(1)
button.click()
time.sleep(1)
driver.close()

#%%
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
# from bs4 import BeautifulSoup # 调用BeautifulSoup库
import time
chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 对浏览器的设置
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') # 访问页面
time.sleep(2) # 等待2秒
label = driver.find_element_by_tag_name('label') # 解析网页并提取第一个<label>标签
print(label.text) # 打印label的文本
driver.close() # 关闭浏览器

# %%
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') # 访问页面
time.sleep(2) # 等待两秒

label = driver.find_element_by_class_name('teacher') # 根据类名找到元素
print(type(label)) # 打印label的数据类型
print(label.get_attribute('type')) # 获取type这个属性的值
driver.close() # 关闭浏览器

# %%
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') # 访问页面
time.sleep(2) # 等待两秒

labels = driver.find_elements_by_tag_name('label') # 根据标签名提取所有元素
print(type(labels))  # 打印labels的数据类型
for label in labels:
    print(label.text) # 打印labels
driver.close() # 关闭浏览器


# %%
"""使用driver的page_source属性获取网页"""
from selenium import webdriver
import time
import bs4
driver = webdriver.Chrome()
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)
page_source = driver.page_source
print(type(page_source))
print(page_source)

driver.close()
bs = bs4.BeautifulSoup(page_source, 'html.parser')
labels = bs.find_all('label')
for label in labels:
    print(labels.text)

# %%
# 本地Chrome浏览器设置方法
from selenium import webdriver # 从selenium库中调用webdriver模块
import time # 调用time模块
driver = webdriver.Chrome() # 设置引擎为Chrome，真实地打开一个Chrome浏览器

driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') # 访问页面
time.sleep(2) # 暂停两秒，等待浏览器缓冲

teacher = driver.find_element_by_id('teacher') # 找到【请输入你喜欢的老师】下面的输入框位置
teacher.send_keys('必须是吴枫呀') # 输入文字
assistant = driver.find_element_by_name('assistant') # 找到【请输入你喜欢的助教】下面的输入框位置
assistant.send_keys('都喜欢') # 输入文字
button = driver.find_element_by_class_name('sub') # 找到【提交】按钮
button.click() # 点击【提交】按钮
time.sleep(1)
driver.close() # 关闭浏览器

# %%
from selenium import webdriver # 从selenium库中调用webdriver模块
import time # 调用time模块
driver = webdriver.Chrome() # 设置引擎为Chrome，真实地打开一个Chrome浏览器
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)
teacher = driver.find_element_by_id('teacher')
teacher.send_keys('吴枫')
time.sleep(2)
assistant = driver.find_element_by_name('assistant')
assistant.send_keys('都喜欢')
time.sleep(2)
btn = driver.find_element_by_class_name('sub')
btn.click()
time.sleep(2)
driver.close()

# %%
"""抓取歌曲评论"""
from selenium import webdriver # 从selenium库中调用webdriver模块
import time # 调用time模块
driver = webdriver.Chrome() # 设置引擎为Chrome，真实地打开一个Chrome浏览器
driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html')
time.sleep(2)
btn = driver.find_element_by_class_name('comment__show_all_link')
btn.click()
time.sleep(2)
hot_comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_hot_text')
i = 1
for comment in hot_comments:
    print('评论{0}'.format(i), comment.text)
    print('\n')
    i+=1
driver.close()

# %%
"""抓取歌曲评论"""
from selenium import webdriver # 从selenium库中调用webdriver模块
import time  # 调用time模块
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类

chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
driver = webdriver.Chrome(options = chrome_options) # 设置引擎为Chrome，在后台默默运行
# driver = webdriver.Chrome() # 设置引擎为Chrome，真实地打开一个Chrome浏览器

driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html') # 访问页面
time.sleep(2)

button = driver.find_element_by_class_name('js_get_more_hot') # 根据类名找到【点击加载更多】
button.click() # 点击
time.sleep(2) # 等待两秒

pageSource = driver.page_source # 获取Elements中渲染完成的网页源代码
soup = BeautifulSoup(pageSource,'html.parser')  # 使用bs解析网页
comments = soup.find('ul',class_='js_hot_list').find_all('li',class_='js_cmt_li') # 使用bs提取元素
print(len(comments)) # 打印comments的数量

for comment in comments: # 循环
    sweet = comment.find('p') # 提取评论
    print ('评论：%s\n ---\n'%sweet.text) # 打印评论
driver.close() # 关闭浏览器 # 关闭浏览器

# %%
from selenium import webdriver # 从selenium库中调用webdriver模块
import time  # 调用time模块

driver = webdriver.Chrome()  # 设置引擎为Chrome，真实地打开一个Chrome浏览器

driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php?checkemail=confirm')
time.sleep(2)
user_login = driver.find_element_by_id('user_login')
user_login.clear()
user_login.send_keys('phoenix228')
time.sleep(2)
password = driver.find_element_by_id('user_pass')
password.clear()
password.send_keys('iloveYOU000')
time.sleep(2)
# btn = driver.find_element_by_name('wp-submit')
btn = driver.find_element_by_id('wp-submit')
# btn = driver.find_element_by_class_name('button')
btn.click()
time.sleep(2)
driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/')
link = driver.find_element_by_id('post-20').find_element_by_class_name('entry-title')
link.click()
time.sleep(2)
driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_03/')
comment = driver.find_element_by_class_name('comment-form-comment').find_element_by_id('comment')
comment.send_keys('学习selenium，测试自动登录进行评论方法')
time.sleep(2)
submit = driver.find_element_by_name('submit')
submit.click()



# %%
from selenium import webdriver # 从selenium库中调用webdriver模块
import time  # 调用time模块

driver = webdriver.Chrome()  # 设置引擎为Chrome，真实地打开一个Chrome浏览器
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)
teacher = driver.find_element_by_id('teacher')
teacher.send_keys('必须是吴枫老师啊')
time.sleep(2)
assistant = driver.find_element_by_name('assistant')
assistant.send_keys('都喜欢')
time.sleep(2)
btn = driver.find_element_by_class_name('sub')
btn.click()
time.sleep(2)
contents = driver.find_elements_by_class_name('content')
for content in contents:
    print(content.text)
    print()

driver.close()

# %%
from selenium import webdriver # 从selenium库中调用webdriver模块
import time  # 调用time模块
from bs4 import BeautifulSoup

driver = webdriver.Chrome()  # 设置引擎为Chrome，真实地打开一个Chrome浏览器
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)
teacher = driver.find_element_by_id('teacher')
teacher.send_keys('必须是吴枫老师啊')
time.sleep(2)
assistant = driver.find_element_by_name('assistant')
assistant.send_keys('都喜欢')
time.sleep(2)
btn = driver.find_element_by_class_name('sub')
btn.click()
time.sleep(2)
pagesource = driver.page_source
soup = BeautifulSoup(pagesource,'html.parser')
contents = soup.find_all(class_='content')
for content in contents:
    print(content.text)
    print()
    
driver.close()