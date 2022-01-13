"""连接有道翻译，编写翻译器"""
import requests,json
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.77'
}
data = {
    'i': input('请输入需要翻译的内容：'),
    'from': 'AUTO',
    'to': 'AUTO',
    'client': 'fanyideskweb',
    'smartresult': 'dict',
    'doctype':'json',
    'keyfrom': 'fanyi.web',
    'action':'FY_BY_REALTlME'
}
# session = requests.session()
res = requests.post(url, headers=headers, data=data)
print(res.status_code)
fanyi = res.json()
result = fanyi['translateResult'][0][0]['tgt']
print('翻译结果：{}'.format(result))