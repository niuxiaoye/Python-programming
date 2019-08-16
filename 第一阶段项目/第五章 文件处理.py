# 练习一
l = []
with open('练习一.txt', 'r', encoding='utf-8') as f1, \
       open('练习一结果.txt', 'w+', encoding='utf-8') as f2:
    # print(f1.read())
    for i in f1:
        if i not in l:
            l.append(i)
    print(l)
    f2.writelines(l)
    print(f2.read())



# 练习三
l = []
with open('练习三.txt', 'r', encoding='utf-8') as f1, \
       open('练习三结果.txt', 'w+', encoding='utf-8') as f2:
    for i in f1:
        for j in i.split('\t'):
            l.append(j)
    print(l)
    l[0] = l[0] + 'albert'
    print(l)
    for k in set(range(0, len(l), 1)) - set(range(2, len(l), 3)):
        l[k] = l[k]+'\t'
    f2.writelines(l)
    print(f2.read())



 