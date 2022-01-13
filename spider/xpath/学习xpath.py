import requests
from lxml import etree
res = requests.get('https://www.pearvideo.com/')
print(res.status_code)
# print(res.text)
res.encoding = 'utf-8'
res_xpath = etree.HTML(res.text)
print(type(res_xpath))
print(res_xpath)
# /text 提取文字
# 绝对路径提取
print(res_xpath.xpath('/html/head/title/text()'))
# // 相对路径提取
print(res_xpath.xpath('//title/text()'))
# //后面是标签的名字
# 对标签指定属性使用@
print(res_xpath.xpath('//a[@href="live" and @class]/text()'))

print('\n指定class属性')
# print(res_xpath.xpath('//a[@class]/text()'))

print('\n指定class属性具体值')
print(res_xpath.xpath('//a[@class="menu"]/text()' ))
print(res_xpath.xpath('body//li/a[1]/text()' ))