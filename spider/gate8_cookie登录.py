#%%
import requests
url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
data = {
'log': 'spiderman',  #写入账户
'pwd': 'crawler334566',  #写入密码
'wp-submit': '登录',
'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
'testcookie': '1'
}#登录信息
log_in = requests.post(url, headers=headers, data=data)
print(log_in)
cookies = log_in.cookies
url1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
data1 = {
'comment': input('请输入你想要发表的评论：'),
'submit': '发表评论',
'comment_post_ID': '24',
'comment_parent': '0'
} #评论信息
comment = requests.post(url1, headers=headers, data=data1, cookies= cookies)
print(comment.status_code)