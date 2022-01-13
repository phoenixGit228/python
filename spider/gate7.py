#%%
# 引入requests和bs
import requests
from bs4 import BeautifulSoup

# 使用headers是一种默认的习惯，默认你已经掌握啦~
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# 发起请求，将响应的结果赋值给变量res。
url='https://www.zhihu.com/people/zhang-jia-wei/posts?page=1'
res=requests.get(url,headers=headers)
# 检查状态码 
print(res.status_code)
# 用bs进行解析
bstitle=BeautifulSoup(res.text,'html.parser')
# 提取我们想要的标签和里面的内容
title=bstitle.find_all(class_='ContentItem-title')
# 打印title
for item in title:
    print(item.find('a').text)

#%%
"""爬取知乎评论"""
import requests, bs4
url = 'https://www.zhihu.com/people/zhang-jia-wei/posts?page=1'

headers = {'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
res = requests.get(url,headers=headers)
# print(res.status_code)
bs = bs4.BeautifulSoup(res.text, 'html.parser')
items = bs.find_all(class_='List-item')
for item in items:
    title = item.find('h2').text
    data = item.find(class_='RichContent-inner').text
    print('标题：', title)
    print("内容：", data)
    print()

url='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles'
params = {
    'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
    'offset': '10',
    'limit':'10',
}
res = requests.get(url,headers=headers,params=params)
# print(res.status_code)
bs_json = res.json()
for data in bs_json['data']:
    title = data['title']
    content = data['excerpt']
    print('标题：',title)
    print("内容：",content)
    print()

# %%
"""爬取知乎评论 20条"""
import requests
# 使用headers是一种习惯
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
# 建立一个空列表，以待写入数据
articlelist=[]
# 设置offset的起始值为第一页的值：10
offset=10

while True:
    # 封装参数
    params={
        'include':'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
        'offset':str(offset),
        'limit':'10',
        'sort_by':'voteups',
        }
    # 发送请求，并把响应内容赋值到变量res里面
    res=requests.get(url,headers=headers,params=params)
    # 确认这个response对象状态正确 
    print(res.status_code)
    # 如果响应成功，继续
    if int(res.status_code) == 200:
        # 用json()方法去解析response对象
        articles=res.json()
        # 定位数据
        data=articles['data']
    
        for i in data:
            # 把数据封装成列表
            list1=[i['title'],i['url'],i['excerpt']]
            articlelist.append(list1) 
        # 在while循环内部，offset的值每次增加20
        offset=offset+20 
        if offset>30:
            break
        # 如果offset大于30，即爬了两页，就停止
        # ——————另一种思路实现———————————————— 
        # 如果键is_end所对应的值是True，就结束while循环。
        #if articles['paging']['is_end'] == True:
            #break
        # ————————————————————————————————————
#打印看看
for i in articlelist:
    print(i)

# %%
import requests
# 引用csv
import csv
# 调用open()函数打开csv文件，传入参数：文件名“articles.csv”、写入模式“w”、newline=''。
csv_file=open('articles.csv','w',newline='',encoding='utf-8')
# 用csv.writer()函数创建一个writer对象。
writer = csv.writer(csv_file)
# 创建一个列表
list2=['标题','链接','摘要']
# 调用writer对象的writerow()方法，可以在csv文件里写入一行文字 “标题”和“链接”和"摘要"。
writer.writerow(list2)
# 使用headers是一种习惯
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
# 设置offset的起始值为10
offset=10

while True:
    # 封装参数
    params={
        'include':'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
        'offset':str(offset),
        'limit':'10',
        'sort_by':'voteups',
        }
    # 发送请求，并把响应内容赋值到变量res里面
    res=requests.get(url,headers=headers,params=params)
    # 确认这个response对象状态正确 
    print(res.status_code)
    # 如果响应成功，继续
    if int(res.status_code) == 200:
        articles=res.json()
        print(articles)
        # 定位数据
        data=articles['data']
    
        for i in data:
            # 把目标数据封装成一个列表
            list1=[i['title'],i['url'],i['excerpt']]
            # 调用writerow()方法，把列表list1的内容写入
            writer.writerow(list1)  
        # 在while循环内部，offset的值每次增加20
        offset=offset+20
        if offset > 30:
            break

# 写入完成后，关闭文件就大功告成
csv_file.close()
print('okay')

# %%
"""爬取知乎评论 前20条"""
import requests
import csv
import openpyxl
# 使用headers是一种习惯
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
# 建立一个空列表，以待写入数据
articlelist=[]
# 设置offset的起始值为第一页的值：10
offset=10
csv_file = open('csv_file.csv', 'w', newline='', encoding='gbk')
writer = csv.writer(csv_file)
writer.writerow(['标题', '链接', '文章'])

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '文章'
sheet['a1'] = '标题'
sheet['b1'] = '链接'
sheet['c1'] = '文章'

while True:
    # 封装参数
    params={
        'include':'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
        'offset':str(offset),
        'limit':'10',
        'sort_by':'voteups',
        }
    # 发送请求，并把响应内容赋值到变量res里面
    res=requests.get(url,headers=headers,params=params)
    # 确认这个response对象状态正确 
    print(res.status_code)
    # 如果响应成功，继续
    if int(res.status_code) == 200:
        # 用json()方法去解析response对象
        articles=res.json()
        # 定位数据
        data=articles['data']
    
        for i in data:
            # 把数据封装成列表
            list1=[i['title'],i['url'],i['excerpt']]
            articlelist.append(list1) 
            writer.writerow(list1)
            sheet.append(list1)
        # 在while循环内部，offset的值每次增加20
        offset=offset+20 
        if offset>30:
            break
        # 如果offset大于30，即爬了两页，就停止
        # ——————另一种思路实现———————————————— 
        # 如果键is_end所对应的值是True，就结束while循环。
        #if articles['paging']['is_end'] == True:
            #break
        # ————————————————————————————————————
#打印看看
wb.save('csv_file.xlsx')
csv_file.close()
#print(articlelist)

# %%
""" 编写扇贝错词本 """
import requests
url = 'https://www.shanbay.com/api/v1/vocabtest/category/?_=1589288404458'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
res = requests.get(url, headers=headers)
# print(res.status_code)
print('单词测试题库：')
res_json = res.json()
res_dict = res_json['data']
for i in range(10):
    print(str(i), res_dict[i][1])
print()
# for resdict in res_dict:
#     print(resdict)
num = input('请选择题库,输入对应数字:')

# %%
