# %%
"""
查快递
"""
import requests
# 调用get方法，下载这个字典
post_number = input("请输入需要查询的快递单号：")

url = 'https://www.kuaidi100.com/query'
headers = {
    'origin':'https://www.kuaidi100.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer':'https://www.kuaidi100.com/all/qy.shtml',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36 Edg/81.0.416.64',
    # 标记了请求从什么设备，什么浏览器上发出
}
params = {
    'type': 'jd',
    'postid' : post_number,
    'temp' : '0.3511843726918964',
    'phone':"",
}
res_post = requests.get(url, headers=headers, params=params)
json_post = res_post.json()
for item in json_post['data']:
    print(item['time']," : ", item['context'])


# %%
import requests
import random
#调用requests模块，负责上传和下载数据

cookie = input('请输入网页的cookie值')
kuaidiType = input('请输入快递类型（拼音)')
kuaidiID = input('请输入快递单号')

url = 'https://www.kuaidi100.com/query?'
#使用get需要一个链接

header = {
'Accept-Encoding': 'gzip, deflate, br',
'referer': 'https://www.kuaidi100.com/',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Connection': 'keep-alive',
'Cookie': cookie,
'Host': 'www.kuaidi100.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}
a = random.random()
params = {
          'type': kuaidiType,
          'postid': kuaidiID,
          'temp':str(a),
          'phone':''
          }
#将需要get的内容，以字典的形式记录在params内

r = requests.get(url, params=params,headers = header)
result = r.json()
for i in result['data']:
    print(i['context'])