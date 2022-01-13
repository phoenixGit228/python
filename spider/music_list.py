#%%
"""
提取歌名、专辑、时长、链接
"""
# 引用requests库   
import requests
# 调用get方法，下载这个字典
res_music : requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct:24&qqmusic_ver:1298&new_json:1&remoteplace:txt.yqq.song&searchid:60997426243444153&t:0&aggr:1&cr:1&catZhida:1&lossless:0&flag_qc:0&p:1&n:20&w:%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk:5381&loginUin:0&hostUin:0&format:json&inCharset:utf8&outCharset:utf-8&notice:0&platform:yqq.json&needNewCode:0')
# 使用json()方法，将response对象，转为列表/字典
json_music = res_music.json()
# 一层一层地取字典，获取歌单列表
list_music = json_music['data']['song']['list']
# list_music是一个列表，music是它里面的元素
for music in list_music:
    # 以name为键，查找歌曲名
    print(music['name'])
    # 查找专辑名
    print('所属专辑：'+music['album']['name'])
    # 查找播放时长
    print('播放时长：'+str(music['interval'])+'秒')
    # 查找播放链接
    print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html\n\n')


    
#%%
"""
提取歌名、专辑、时长、链接
"""
# 引用requests库   
import requests
# 调用get方法，下载这个字典
res_music : requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct:24&qqmusic_ver:1298&new_json:1&remoteplace:txt.yqq.song&searchid:60997426243444153&t:0&aggr:1&cr:1&catZhida:1&lossless:0&flag_qc:0&p:1&n:20&w:%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk:5381&loginUin:0&hostUin:0&format:json&inCharset:utf8&outCharset:utf-8&notice:0&platform:yqq.json&needNewCode:0')
# 使用json()方法，将response对象，转为列表/字典
json_music = res_music.json()
# 一层一层地取字典，获取歌单列表
list_music = json_music['data']['song']['list']
# list_music是一个列表，music是它里面的元素
for music in list_music:
    # 以name为键，查找歌曲名
    print("歌曲名：", music['name'])
    print("专辑：", music['album']['name'])
    minute = int(music['interval'])//60
    sec = int(music['interval'])%60
    print("播放时长：{}分{}秒".format(minute, sec))
    print("播放链接：", music['mid'],'\n')

# %%
"""
爬取精彩评论
"""
import requests
# 引用requests模块
for i in range(3):
    url : "https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk:5381&loginUin:0&hostUin:0&format:json&inCharset:utf8&outCharset:GB2312&notice:0&platform:yqq.json&needNewCode:0&cid:205360772&reqtype:2&biztype:1&topid:102065756&cmd:6&needmusiccrit:0&pagenum:"+str(i)+"&pagesize:15&lasthotcommentid:song_102065756_3202544866_44059185&domain:qq.com&ct:24&cv:10101010"
    res_comments = requests.get(url)
    # 调用get方法，下载评论列表
    json_comments = res_comments.json()
    # 使用json()方法，将response对象，转为列表/字典
    list_comments = json_comments['comment']['commentlist']
    # 一层一层地取字典，获取评论列表
    for comment in list_comments:
    # list_comments是一个列表，comment是它里面的元素
        print(comment['rootcommentcontent'])
        # 输出评论
        print('-----------------------------------')
        # 将不同的评论分隔开来

# %%
"""
爬取精彩评论
"""
import requests
# 引用requests模块
url : 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'
# 请求歌曲评论的url参数前面的部分

for i in range(5):
    params : {
    'g_tk':'5381',
    'loginUin':'0', 
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'GB2312',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0',
    'cid':'205360772',
    'reqtype':'2',
    'biztype':'1',
    'topid':'102065756',
    'cmd':'6',
    'needmusiccrit':'0',
    'pagenum':str(i),
    'pagesize':'15',
    'lasthotcommentid':'song_102065756_3202544866_44059185',
    'domain':'qq.com',
    'ct':'24',
    'cv':'10101010'   
    }
    # 将参数封装为字典
    res_comments = requests.get(url,params=params)
    # 调用get方法，下载这个字典
    json_comments = res_comments.json()
    list_comments = json_comments['comment']['commentlist']
    for comment in list_comments:
        print(comment['rootcommentcontent'])
        print('-----------------------------------')

# %%
"""
爬取歌单
"""
import requests
url : 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'

headers : {
    'origin':'https://y.qq.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }
# 伪装请求头

params : {
'ct':'24',
'qqmusic_ver': '1298',
'new_json':'1',
'remoteplace':'sizer.yqq.song_next',
'searchid':'64405487069162918',
't':'0',
'aggr':'1',
'cr':'1',
'catZhida':'1',
'lossless':'0',
'flag_qc':'0',
'p':'1',
'n':'20',
'w':'周杰伦',
'g_tk':'5381',
'loginUin':'0',
'hostUin':'0',
'format':'json',
'inCharset':'utf8',
'outCharset':'utf-8',
'notice':'0',
'platform':'yqq.json',
'needNewCode':'0'    
}
# 将参数封装为字典
res_music = requests.get(url,headers=headers,params=params)
# 发起请求，填入请求头和参数

#%%
"""
抓取歌词
"""
import requests
# 调用get方法，下载这个字典
for i in range(1):
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
    headers = {
        'origin':'https://y.qq.com',
        # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
        'referer':'https://y.qq.com/portal/search.html',
        # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        # 标记了请求从什么设备，什么浏览器上发出
    }
    params = {
        'ct' : '24',
        'qqmusic_ver' : '1298',
        'new_json' : '1',
        'remoteplace' : 'txt.yqq.song',
        'searchid' : '56880579804232225',
        't' : '0',
        'aggr' : '1',
        'cr' : '1',
        'catZhida' : '1',
        'lossless' : '0',
        'flag_qc' : '0',
        'p' : str(i),
        'n' : '10',
        'w': '周杰伦',
        'g_tk_new_20200303': '5381',
        'g_tk' : '5381',
        'loginUin' : '0',
        'hostUin' : '0',
        'format' : 'json',
        'inCharset' : 'utf8',
        'outCharset' : 'utf-8',
        'notice' : '0',
        'platform' : 'yqq.json',
        'needNewCode' : '0',
    }

    res_music = requests.get(url, headers=headers, params=params)
    # print(res_music.status_code)
    # 使用json()方法，将response对象，转为列表/字典
    json_music = res_music.json()
    # 一层一层地取字典，获取歌单列表
    list_music = json_music['data']['song']['list']
    # list_music是一个列表，music是它里面的元素
    for music in list_music:
        # 以name为键，查找歌曲名
        print("歌曲名：", music['name'])
        print("专辑：", music['album']['name'])
        minute = int(music['interval'])//60
        sec = int(music['interval'])%60
        print("播放时长：{}分{}秒".format(minute, sec))
        # print("播放链接：", music['mid'],'\n')
        song_link = 'https://y.qq.com/n/yqq/song/'+music['mid']+'.html' 
        print('播放链接：', song_link )
        # res_song_link=bs4.BeautifulSoup(song_link,'html.parser')
        # lyric = res_song_link.find(id='lrc-content')
        # print(type(lyric))
        url2 = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
        params = {
            'nobase64': '1',
            'musicid': music['id'],
            '-' : 'jsonp1',
            'g_tk_new_20200303': '5381',
            'g_tk': '5381',
            'loginUin': '0',
            'hostUin': '0',
            'format': 'json',
            'inCharset': 'utf8',
            'outCharset': 'utf-8',
            'notice': '0',
            'platform': 'yqq.json',
            'needNewCode': '0',
        }
        song_lyric = requests.get(url2, headers=headers, params=params)
        song_lyric_json = song_lyric.json()
        lyric = song_lyric_json['lyric']
        print('歌词：\n', lyric,'\n\n')


