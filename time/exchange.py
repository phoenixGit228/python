# * -- using coding - utf-8 --*
import time
print('小精灵：您好，欢迎来到古灵阁，请问您需要帮助吗？需要or不需要？')
help = input('你：')
if help == '不需要':
    print('小精灵：好的，再见')
else:
    print('小精灵：请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询')
    choice = int(input('你：'))
    
    if choice == 1:
        print('小精灵：推荐你去存取款窗口')
    elif choice == 2:
        print('小精灵：金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币')
        time.sleep(2)
        print('小精灵：请问您需要兑换多少金加隆呢？')
        num = int(input("你："))
        print('小精灵：好的，我知道了，您需要兑换' + str(num) + '金加隆。')
        time.sleep(2)
        print('小精灵：那么，您需要付给我' + str(num * 51.3) + '人民币。')
    else:
        print('小精灵：推荐你去咨询窗口')
    