#%%
from selenium import webdriver  #从selenium库中调用webdriver模块
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

options = Options()
options.page_load_strategy = 'eager'

driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome() # 设置引擎为Chrome，真实地打开一个Chrome浏览器
driver.get('https://wenku.baidu.com/view/6cbbd6f29f3143323968011ca300a6c30c22f19e.html',)
time.sleep(5)
# ok
# pages = driver.find_elements_by_class_name('reader-txt-layer')
# driver.find_element_by_xpath('//*[@id="html-reader-go-more"]/div[2]/div[1]/span/span[2]').click()
driver.find_element_by_class_name('page-input')
time.sleep(5)
# pg = driver.page_source
# soup = BeautifulSoup(pg, 'lxml')
# pages = soup.find_all(class_='ie-fix')
pages = pages.find_elements_by_class_name(class_='ie-fix')
for page in pages:
    print(page,'\n\n')
# words = []
# for page in pages:
#     word = page.find_all('p')
#     for i in word:
#         txt = i.text
#         # print(txt)
#         if 'Lesson' in txt:
#                 txt = f'\n\n{txt}'
#         words.append(txt)
        
# txt = ''.join(words)
# txt.replace('课文及翻译','课文及翻译\n\n')
# print(txt)
driver.quit()

#%%
from selenium import webdriver  #从selenium库中调用webdriver模块
import time
from selenium.webdriver.chrome.options import Options


# 使用with函数，自动判断是否需要关闭/结束
with webdriver.Chrome() as driver:
    driver.get('https://wenku.baidu.com/view/6cbbd6f29f3143323968011ca300a6c30c22f19e.html',)
    # 设置窗口大小
    driver.set_window_size(1024, 768)
    # 窗口大小
    width = driver.get_window_size().get('width')
    height = driver.get_window_size().get('height')
    print(width, height)
    # 窗口尺寸
    size = driver.get_window_size()
    width = size.get('width')
    height = size.get('height')
    print(width, height)
    time.sleep(5)
    # 设置窗口位置
    driver.set_window_position(1024,768)    
    # 获取窗口位置
    x = driver.get_window_position().get('x')
    y = driver.get_window_position().get('y')
    print('窗口位置', x, y)
    # 获取窗口位置    
    position = driver.get_window_position()
    x = position.get('x')
    y = position.get('y')
    print('窗口位置：', x, y)
    time.sleep(5)
    #最大化窗口
    driver.maximize_window()
    time.sleep(5)
    #最小化窗口
    driver.minimize_window()
    time.sleep(5)
    #全屏窗口
    driver.fullscreen_window()
    time.sleep(5)
    # driver.switch_to.frame('html-reader-go-more')
    # button = driver.find_element_by_id('html-reader-go-more').    find_element_by_class_name('banner-more-btn')
    driver.find_element_by_class_name('banner-more-btn').click()
    driver.switch_to.default_content()
    # time.sleep(2)
    # ok
    pages = driver.find_elements_by_class_name('ie-fix')
    words = []
    for page in pages:
        word = page.find_elements_by_tag_name('p')
        for i in word:
            txt = i.text
            # print(txt)
            if 'Lesson' in txt:
                    txt = f'\n\n{txt}\n\n'
            words.append(txt)
            
    txt = ''.join(words)
    txt.replace('课文及翻译','课文及翻译\n\n')
    print(txt)
