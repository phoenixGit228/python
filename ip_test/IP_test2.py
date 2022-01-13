with open('IP1.txt', 'r', encoding='utf8') as f1:
    line1 = f1.readlines()

with open('IP2.txt', 'r', encoding='utf8') as f2:
    line2 = f2.readlines()

print(line1)
print(line2)

tmp = []

for tmp1 in line1:
    for tmp3 in line2:
        if tmp1 == tmp3:
            tmp.append(tmp1)

with open('IP_same.txt', 'w', encoding='utf8') as f3:
    for line in tmp:
        f3.write(line)
