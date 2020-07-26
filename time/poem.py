list_test = ['一弦一柱思华年。\n','只是当时已惘然。\n']

with open ('poem1.txt','r',encoding='utf8') as f:
    lines = f.readlines()

with open('poem2.txt','w',encoding='utf8') as new:
    for line in lines:
        if line in list_test:
            new.write('____________。\n')
        else:
            new.write(line)
