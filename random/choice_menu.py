import random
import time

welcome = '------  客官，欢迎自动选餐程序 -------'
print(welcome)
# while True:
#     print('\r',welcome,end="",flush=True)
#     welcome = welcome[1:] + welcome[0]
#     time.sleep(0.25)

choice1 = input('请问客官是不知道吃什么，还是在几家店中犹豫呢？\n1-不知道吃什么；2-在几家店中犹豫  \n')

if choice1 == '1':  # 不知道吃什么
    # time.sleep(1)
    menu = [['面条', '米饭', '凉皮', '包子'],
            ['拍黄瓜', '海带丝', '卤鸡翅', '小咸菜', '茶鸡蛋']]
    aa = []
    bb = []

    def shanchu(xx,yy):
        xulie = xx.index(yy)
        del xx[xulie]

    while True:
        try:
            zhusi = random.choice(menu[0])
            print('小二为客官推荐主食：{}'.format(zhusi))
            a = input('请问是否满意推荐：y-满意，其他-不满意\n')
            if a == 'y':
                aa.append(zhusi)
                b = input('请问是否还要其他主食，y-是的，其他-不要了\n')
                if b == 'y':
                    shanchu(menu[0],zhusi)
                else:
                    break
            else:
                shanchu(menu[0],zhusi)
        except IndexError:
            print('那再为你推荐些小菜吧')
            break
    zhusi2= ','.join(aa)
    print('现在为你推荐些小菜')

    while True:
        try:
            xiaocai = random.choice(menu[1])
            print('小二为客官推荐小菜：{}'.format(xiaocai))
            a = input('请问是否满意推荐：y-满意，其他-不满意\n')
            if a == 'y':
                bb.append(xiaocai)
                b = input('请问是否还要其他主食，y-是的，其他-不要了\n')
                if b == 'y':
                    shanchu(menu[1],xiaocai)
                else:
                    break
            else:
                shanchu(menu[1],xiaocai)
        except IndexError:
            print('很抱歉，未能推荐满意的小菜')
            break
    xiaocai2 = ','.join(bb)
    print('客官，您点的菜为-主食：{0}，小菜：{1}'.format(zhusi2,xiaocai2))
else:
    # diner_list = ['和府捞面', '伏牛堂', '牛街老爆肚满', '丰泽园', '关东煮']
    diner = []

    select = input('请问客官在哪几家饭店中犹豫呢？\n')

    while True:
        diner.append(select)
        q = input('请问还有吗？y-是的，其他-没有\n')
        if q == 'y':
            select = input('请输入餐馆名称: ')
        else:
            break

    while True:
        try:
            select = random.choice(diner)
            xulie = diner.index(select)
            print('小二为客官推荐：{}'.format(select))
            choice2 = input('结果是否满意：y-满意，其他-不满意\n')
            if choice2 == 'y':
                break
            else:
                del (diner[xulie])
            # print(diner_list)
        except IndexError:
            print('很抱歉，未能给客官推荐满意餐馆\n')
            break
print('\n感谢客官使用，欢迎常来\n')
    