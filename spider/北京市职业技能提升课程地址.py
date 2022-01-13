#%%
# # !打开课程页
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv

chrome_options = Options()
chrome_options.page_load_strategy = 'eager'
# options.add_argument('start-maximized')
# chrome_options.add_argument('auto-open-devtools-for-tabs')
chrome_options.add_argument('--headless')
with webdriver.Chrome(chrome_options=chrome_options) as driver:
    driver.get('https://www.bjjnts.cn/login')
    # time.sleep(1)
    driver.maximize_window()
    # time.sleep(1)
    driver.find_element_by_name('username').send_keys('410721198202283516')
    # time.sleep(1)
    driver.find_element_by_name('password').send_keys('bj123465')
    # time.sleep(1)
    driver.find_element_by_class_name('login_btn').click()
    time.sleep(5)
    driver.get('https://www.bjjnts.cn/userCourse')
    # time.sleep(3)
    courses = driver.find_element_by_class_name('user_courselist').find_elements_by_tag_name('li')
    print(f'共有{len(courses)}个课程')
    n = 0
    hours = 0
    csv_file = open('course.csv','w',newline='',encoding='gbk')
    writer = csv.writer(csv_file)
    writer.writerow(['序号','课程名称','时长'])
    for course in courses:
        n = n+1
        title = course.find_element_by_tag_name('h2').text
        tm = course.find_element_by_class_name('user_coursedesc').text
        tim = tm[-8:-1].split(':')
        hour = int(tim[0]) + int(tim[1]) / 60.0 + int(tim[2])/3600
        hours += hour
        number = f'课程{n}'
        print(f'课程{n}：{title}\t时长：{hour:2.2f}小时')
        writer.writerow([n, title, hour])
        # print(f'时长{hour:8.2f}小时')
    print(f'总课时{hours:8.2f}小时')
    csv_file.close()
        