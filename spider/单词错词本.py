""" 编写扇贝错词本 """
import requests
import random
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
    print(str(i), res_dict[i][1], end=';  ')
print()
# for resdict in res_dict:
#     print(resdict)
num = input('请选择题库,输入对应数字:')
num = int(num)
url2 = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/'
# https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category=GMAT&_=1589288407937
params = {
    'catagory': res_dict[i][1]
}
res2 = requests.get(url2, headers=headers, params=params)
res2_json = res2.json()
words = res2_json['data']
# 创建一个列表，记录认识的单词
word_know = []
# 创建一个空的列表，用于记录用户不认识的单词。
word_not_know = []
# 识错的单词
word_no = []
# 识对的单词
word_yes = []
# 启动一个循环，循环的次数等于单词的数量。
for word in words:    
    # 记得加一个\n，用于换行。
    print(word['content'])
    # 让用户输入自己是否认识。
    ans = input('请问是否认识：y-认识；其他-不认识\n')
    # 如果用户认识：
    if ans == 'y':
        word_know.append(word['content'])
        # 就把这个单词，追加进列表words_knows。
        i = 1
        for item in word['definition_choices']:
            print('{}.  {}'.format(i,item['definition']))
            i +=1
        choice = int(input('请选择词义：1,2,3,4\n'))
        if word['definition_choices'][choice-1]['rank'] == word['rank']:
            word_yes.append(word['content'])
        else:
            word_no.append(word['content'])
    else:
    # 否则
        word_not_know.append(word['content'])
        # 就把这个单词，追加进列表not_knows。 
    print()
print('\n\n不认识的单词共有{}个:'.format(len(word_not_know)))
print('  '.join(word_not_know))
print('\n认识的单词共有{}个:'.format(len(word_know)))
print('  '.join(word_know))
print('\n认对的单词共有{}个:'.format(len(word_yes)))
print('  '.join(word_yes))
print('\n认错的单词共有{}个:'.format(len(word_no)))
print('  '.join(word_no))

#%%
# 打印一个统计数据：这么多单词，认识几个，认识的有哪些？
#我帮你预置了前几步代码，你可以在此基础上完成本关卡任务。

import requests, csv

# 先用requests请求链接
link = requests.get('https://www.shanbay.com/api/v1/vocabtest/category/')
# 解析请求得到的响应
js_link = link.json()

# 让用户选择自己想测的词库，输入数字编号。int()来转换数据类型
bianhao = int(input('''请输入你选择的词库编号，按Enter确认
1，GMAT  2，考研  3，高考  4，四级  5，六级
6，英专  7，托福  8，GRE  9，雅思  10，任意
>'''))
# 利用用户输入的数字编号，获取题库的代码。如果以输入“高考”的编号“3”为例，那么ciku的值就是，在字典js_link中查找data的值，data是一个list，查找它的第bianhao-1，也就是第2个元素，得到的依然是一个list，再查找该list的第0个元素。最后得到的就是我们想要的NCEE。
ciku = js_link['data'][bianhao-1][0]
# 请求（获取）用于测试的50个单词。
test = requests.get('https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+ciku)
# 对响应test进行解析。
words = test.json()
# 新增一个list，用于统计用户认识的单词
danci = []
# 创建一个空的列表，用于记录用户认识的单词。
words_knows = []
# 创建一个空的列表，用于记录用户不认识的单词。
not_knows = []

print ('测试现在开始。如果你认识这个单词，请输入Y，否则直接敲Enter：')

# 启动一个循环，循环的次数等于单词的数量。
n=0
for x in words['data']:
    n=n+1  
    print ("\n第"+str(n)+'个：'+x['content']) # 加一个\n，用于换行。
    # 让用户输入自己是否认识。
    answer = input('认识请敲Y，否则敲Enter：')
     # 如果用户认识：
    if answer.upper() == 'Y': 
        danci.append(x['content'])
        # 就把这个单词，追加进列表words_knows。
        words_knows.append(x)
        
    # 否则
    else:
        # 就把这个单词，追加进列表not_knows。
        not_knows.append(x)
        
print ('\n在上述'+str(len(words['data']))+'个单词当中，有'+str(len(danci))+'个是你觉得自己认识的，它们是：')
print(danci)

print ('现在我们来检测一下，你有没有真正掌握它们：')
wrong_words = []
right_num = 0
for y in words_knows:
    # 我们改用A、B、C、D，不再用rank值
    print('\n\n'+'A:'+y['definition_choices'][0]['definition'])
    print('B:'+y['definition_choices'][1]['definition'])
    print('C:'+y['definition_choices'][2]['definition'])
    print('D:'+y['definition_choices'][3]['definition'])
    xuanze = input('请选择单词\"'+y['content']+'\"的正确翻译（输入字母即可）：')
    # 我们创建一个字典，搭建起A、B、C、D和四个rank值的映射关系。
    dic = {'A':y['definition_choices'][0]['rank'],'B':y['definition_choices'][1]['rank'],'C':y['definition_choices'][2]['rank'],'D':y['definition_choices'][3]['rank']} 
    # 此时dic[xuanze]的内容，其实就是rank值，此时的代码含义已经和之前的版本相同了。
    if dic[xuanze] == y['rank']:
        right_num += 1
    else:
        wrong_words.append(y)

print('不认识单词：{}个；认识单词：{}个；掌握{}个；错了{}个'.format(len(not_knows), len(word_knows), right_num, len(wrong_words))

# print('错题集：')
with open('wrong_words.csv', 'w', encoding='utf-8') as file1:
    writer = csv.writer(file1)
    for y in wrong_words:
        writer.writerow('请选择单词\"'+y['content']+'\"的正确翻译（输入字母即可）：')
        writer.writerow('A:'+y['definition_choices'][0]['definition'])
        writer.writerow('B:'+y['definition_choices'][1]['definition'])
        writer.writerow('C:'+y['definition_choices'][2]['definition'])
        writer.writerow('D:' + y['definition_choices'][3]['definition'])
        writer.writerow('\n')

    

# %%
import requests,json
session = requests.session()
#创建会话。
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
#添加请求头，避免被反爬虫。
try:
#如果能读取到cookies文件，执行以下代码，跳过except的代码，不用登录就能发表评论。
    cookies_txt = open('cookies.txt', 'r')
    #以reader读取模式，打开名为cookies.txt的文件。
    cookies_dict = json.loads(cookies_txt.read())
    #调用json模块的loads函数，把字符串转成字典。
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    #把转成字典的cookies再转成cookies本来的格式。
    session.cookies = cookies
    #获取cookies：就是调用requests对象（session）的cookies属性。

except FileNotFoundError:
#如果读取不到cookies文件，程序报“FileNotFoundError”（找不到文件）的错，则执行以下代码，重新登录获取cookies，再评论。

    url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
    #登录的网址。
    data = {'log': input('请输入你的账号:'),
            'pwd': input('请输入你的密码:'),
            'wp-submit': '登录',
            'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
            'testcookie': '1'}
    #登录的参数。
    session.post(url, headers=headers, data=data)
    #在会话下，用post发起登录请求。

    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    #把cookies转化成字典。
    cookies_str = json.dumps(cookies_dict)
    #调用json模块的dump函数，把cookies从字典再转成字符串。
    f = open('cookies.txt', 'w')
    #创建名为cookies.txt的文件，以写入模式写入内容
    f.write(cookies_str)
    #把已经转成字符串的cookies写入文件
    f.close()
    #关闭文件

url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
#文章的网址。
data_1 = {
'comment': input('请输入你想评论的内容：'),
'submit': '发表评论',
'comment_post_ID': '13',
'comment_parent': '0'
}
#评论的参数。
comment = session.post(url_1,headers=headers,data=data_1)
#在创建的session下用post发起评论请求，放入参数：文章网址，请求头和评论参数，并赋值给comment。
print(comment.status_code)
#打印comment的状态码

#%%
import requests, csv, json
def cookie_read(file):
    file += '.txt'
    f1 = open('{}'.format(file), 'r')
    print(f1.read())

cookie_read('cookies')

# %%
import requests, json
session = requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

def cookies_read():
    cookies_txt = open('cookies.txt', 'r')
    cookies_dict = json.loads(cookies_txt.read())
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    return (cookies)
    # 以上4行代码，是cookies读取。

def sign_in():
    url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
    data = {'log': input('请输入你的账号'),
            'pwd': input('请输入你的密码'),
            'wp-submit': '登录',
            'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
            'testcookie': '1'}
    session.post(url, headers=headers, data=data)
    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    cookies_str = json.dumps(cookies_dict)
    f = open('cookies.txt', 'w')
    f.write(cookies_str)
    f.close()
    # 以上5行代码，是cookies存储。


def write_message():
    url_2 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
    data_2 = {
        'comment': input('请输入你要发表的评论：'),
        'submit': '发表评论',
        'comment_post_ID': '13',
        'comment_parent': '0'
    }
    return (session.post(url_2, headers=headers, data=data_2))
    #以上9行代码，是发表评论。

try:
    session.cookies = cookies_read()
    # print(session)
except FileNotFoundError:
    sign_in()

num = write_message()
if num.status_code == 200:
    print('成功啦！')
else:
    sign_in()
    num = write_message()

# %%
