"""
抓取歌词
"""
import requests
import html
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
        'p' : str(i+1),
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
        lyric = html.unescape(song_lyric_json['lyric'])
        print('歌词：\n', lyric,'\n\n')