#%%
# # !打开课程页
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

options = Options()
options.page_load_strategy = 'eager'
# options.add_argument('start-maximized')
options.add_argument('auto-open-devtools-for-tabs')
# options.add_argument('--headless')
with webdriver.Chrome(chrome_options=options) as driver:
    driver.get('https://www.bjjnts.cn/login')
    time.sleep(1)
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_name('username').send_keys('410721198202283516')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('bj123465')
    time.sleep(1)
    driver.find_element_by_class_name('login_btn').click()
    time.sleep(3)

    s = requests.Session()
    cookies = driver.get_cookies()
    for cookie in cookies:
        s.cookies.set(cookie['name'], cookie['value'])

    driver.get('https://www.bjjnts.cn/lessonStudy/160/3426')
    time.sleep(3)
    courses = driver.find_element_by_class_name('course_study_videomenu').find_elements_by_tag_name('li')
    print(f'该课程共有{len(courses)}个视频')
    n = 0
    print(courses)
    for course in courses:
        n = n+1
        tm = course.find_element_by_class_name('course_study_menutitle').text
        tim = tm[-9:-1].split(':')
        sec = int(tim[0]) * 3600 + int(tim[1]) * 60 + int(tim[2])
        print(f'视频时长{sec}秒')
        # if(n >7):
        course.find_element_by_class_name('course_study_menutitle').click()
        # time.sleep(3)
        # for i in range(3):
        #     driver.refresh()
        #     time.sleep(2)
        driver.implicitly_wait(5)
        js = "document.querySelector('video').playbackRate=4;"
        driver.execute_script(js)
        time.sleep(3)
        i = 0
        while True:
            i += 1
            time.sleep(1)
            if i >= sec/3.0:
                break
            print('\r',f'时间计时：{i}秒',end='',flush=True)
    
        