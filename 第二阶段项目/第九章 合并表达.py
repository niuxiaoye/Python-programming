'''
练习一

将names=['albert', 'james', 'kobe', 'kd']中的名字全部变成大写

'''
names=['albert', 'james', 'kobe', 'kd']
up_name = []

def upper_names(l):
    for item in l :
        up_name.append(item.upper())

upper_names(names)
print(up_name)



'''
练习二

将names=['albert', 'jr_shenjing', 'james', 'kobe', 'kd']中以sehnjing结尾的名字过滤掉
然后保存剩下的名字长度

'''
names = ['albert', 'jr_shenjing', 'james', 'kobe', 'kd']

names_len = map(lambda name: len(name), list(filter(lambda item: not item.endswith('shenjing'), names)))

print(list(names_len))



'''
练习三

求文件a.txt中最长的行的长度（长度按字符个数算，需要使用max函数）

'''
f_list = []
with open('a.txt', 'r', encoding='utf-8') as f:
    for line in f:
        f_list.append(line)
    print(len(max(f_list)))



'''
练习四

文件shopping.txt内容如下，分别代表商品、价格和数量
    mac,20000,3
    lenovo,3000,10
    bmw,1000000,10
    chicken,200,1
问：
    1. 总共花了多少钱？
    2. 打印出所有商品的信息，格式为[{'name':'XXX', 'price':'333', 'count':3}...]
    3. 单价大于10000的商品信息，格式同上

'''
shop_num = 0
with open('shopping.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line_list = list(line.split(','))
        shop_num = shop_num + int(line_list[1]) * int(line_list[2])
        print('name:{}  price:{}  count:{}'.format(line_list[0], line_list[1], line_list[2]))
    print('总花费金额', shop_num)
    
with open('shopping.txt', 'r', encoding='utf-8') as f:    
    for line in f:
        line_list = list(line.split(','))
        if int(line_list[1]) > 10000:
            print('单价大于一万的商品信息 \n name:{}  price:{}  count:{}'.format(line_list[0], line_list[1], line_list[2]))
    













