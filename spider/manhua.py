#%%
"""
爬取漫画，根据回目自动创建目录，保存该回目的漫画
"""
import requests
import time
import os

# url = "http://img.17dm.com/wugengji/manhua/3b26/35.jpg"

# 第三部漫画，图片链接前缀
str1 = "http://img.17dm.com/wugengji/manhua/3b"

"https://img.wubizigeng.com/mhfile/doupocangqiong/111451/3.jpg"
# "https://img.wubizigeng.com/mhfile/doupocangqiong/1227226/21.jpg"

for i in range(111451, 111910): # 111451，341话；111910 800话
    # 自动创建回目文件夹
    os.mkdir(str(i))
    for j in range(1, 36):
        url = str1 + str(i) + '/' + str(j) + '.jpg'
        # print(url)
        # 获取图片地址
        res = requests.get(url)
        # 图片编号，如果图片序号小于10，序号前加 0
        if j // 10 < 0.5:
            str2 = '0'
        # 方法1：图片路径及命名
        # pic = './'+ str(i) + '/' + str(i) + str2 + str(j)
        # 方法2：图片路径及命名
        pic = './{0}/{0}_{1}{2}'.format(str(i), str2, str(j))
        # 保存漫画
        if res.status_code == 200:
            with open(pic+'.jpg', 'wb') as img:
                img.write(res.content)

        time.sleep(3)
