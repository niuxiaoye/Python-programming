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

# 练习一参考答案一
import os

with open('db.txt', 'r', encoding='utf-8') as read_f, \
        open('db.txt.swap', 'w', encoding='utf-8') as write_f:
    s = set()
    for line in read_f:
        if line not in s:
            s.add(line)
            write_f.write(line)
os.remove('db.txt')
os.rename('db.txt.swap', 'db.txt')



# 练习二参考答案一
import sys

list1 = sys.argv  # 把命令行中解释器后空格分割的所有参数都存成列表  
print(list1) # ???

src_file_path = list1[1]
dst_file_path = list1[2]
# print(src_file_path)
# print(dst_file_path)

with open(r'%s' % src_file_path, mode='rb') as src_f, \
        open(r'%s' % dst_file_path, mode='wb') as dst_f:
    for line in src_f:
        dst_f.write(line)
        


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

# 练习三参考答案一
# 1、先把文件内容全部读入内存
# 2、然后在内存中完成修改
# 3、再把修改后的结果覆盖写入原文件
# 缺点：会在文件内容过大的情况下，占用过多的内存

with open('user.txt', mode='r', encoding='utf-8') as f:
    data = f.read()
    data = data.replace('马一特', '马一特[Albert]')

with open('user.txt', mode='w', encoding='utf-8') as f:
    f.write(data)

# 练习三参考答案二
# 以读的方式打开原文件，以写的方式打开一个新文件,一行一行的读入文件内容
import os

with open('user.txt', mode='rt', encoding='utf-8') as read_f, \
        open('user.txt.swap', mode='wt', encoding='utf-8') as write_f:
    for line in read_f:
        if '马一特' in line:
            line = line.replace('马一特', '马一特[Albert]')

        write_f.write(line)

os.remove('user.txt')
os.rename('user.txt.swap', 'user.txt')

 