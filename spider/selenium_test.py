#%%
# # 从selenium导入webdriver
from selenium import webdriver
import time

# 创建webdriver实例
driver = webdriver.Chrome()

try:
    # 导航地址
    driver.get('https://www.baidu.com')

    # 获取当前url
    url = driver.current_url
    print(url)

    # 浏览器后退
    driver.back()
    time.sleep(2)

    # 浏览器向前
    driver.forward()
    time.sleep(2)

    # 浏览器刷新
    driver.refresh()
    time.sleep(2)

    # 网页title
    title = driver.title
    print(title)
    time.sleep(2)

    # 网页handle
    handle = driver.current_window_handle
    print(handle)
except:
    pass
finally:
    # 关闭浏览器,
    # !close和quit都可以关闭浏览器，
    # !如果存在多个窗口，close只会关闭当前窗口，quit则会关闭所有窗口
    # !对于firefox，chrome浏览器，close不会清除浏览器创建的配置文件，quit则会主动清除
    # driver.close()
    driver.quit()

#%%
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# start webdriver
# using with keyword, WebDriver will automatically quit after indentation
with webdriver.Chrome() as driver:
    #open url
    driver.get('https://www.baidu.com/')

    # Setup wait for later
    wait = WebDriverWait(driver, 10)

    # Store the ID of the original current_window_handle
    original_window = driver.current_window_handle
    print(original_window)
    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1
    
    #click the link which opens in a new tab
    driver.switch_to.new_window('tab')
    #click the link which opens in a new window
    driver.switch_to.new_window('window')
    driver.switch_to.window(original_window)
    # wait for the new window or tab
    wait.until(EC.number_of_windows_to_be(3))

    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        print(window_handle)
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
        time.sleep(2)
        # driver.close()

    # wait for the new tab to finish loading content
    # wait.until(EC.title_is('百度一下，你就知道'))

#%%
from selenium import webdriver

with webdriver.Chrome() as driver:
    driver.get('https://www.selenium.dev/documentation/en/webdriver/browser_manipulation/')
    driver.find_element_by_tag_name('button').click()

#%%
# !登录北京市职业技能培训网站
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.page_load_strategy = 'eager'
with webdriver.Chrome(chrome_options=options) as driver:
    driver.get('https://www.bjjnts.cn/login')
    driver.maximize_window()
    driver.find_element_by_name('username').send_keys('410721198202283516')
    driver.find_element_by_name('password').send_keys('bj123465')
    driver.find_element_by_class_name('login_btn').click()
    time.sleep(3)
    driver.find_element_by_class_name('my_course').click()
    time.sleep(5)
    courses = driver.find_elements_by_tag_name('li')
    print(courses)
    for x in courses:
        txt = x.find_elemnet_by_class_name('user_coursetext').text
        if '管理思想史' in txt:
            x.find_element_by_class_name('user_coursepic').click()
    
    time.sleep(5)

    # driver.get('https://www.bjjnts.cn/lessonStudy/184/3534')
    # times = driver.find_element_by_class_name('new_demotop').find_elements_by_tag_name('li')
    # print(times.text)

#%%
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.page_load_strategy = 'eager'
with webdriver.Chrome(chrome_options=options) as driver:
    driver.maximize_window()
    driver.get('https://www.bjjnts.cn/lessonStudy/184/3534')
    time.sleep(5)
    courses = driver.find_element_by_class_name('course_study_videomenu').find_elements_by_tag_name('li')
    for course in courses:
        tm = course.find_element_by_class_name('course_study_menutitle').text
        print(tm)
    time.sleep(5)

    # times = driver.find_element_by_class_name('new_demotop').find_elements_by_tag_name('li')
    # print(times.text)


# %%


