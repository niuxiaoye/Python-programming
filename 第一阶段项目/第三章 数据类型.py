# 练习一
name = " alberT"
# 1 移除 name 变量对应的值两边的空格,并输出处理结果
print(name.strip())
# 2 判断 name 变量对应的值是否以 "al" 开头,并输出结果
print(name.strip().find('al', 0, 2))
print(name.startswith('al'))
# 3 判断 name 变量对应的值是否以 "T" 结尾,并输出结果
print(name.strip().find('T', -1))
print(name.endswith('T'))
# 4 将 name 变量对应的值中的 “l” 替换为 “p”,并输出结果
print(name.replace('l', 'p'))
# 5 将 name 变量对应的值根据 “l” 分割,并输出结果。
print(name.split('l'))
# 6 将 name 变量对应的值变大写,并输出结果
print(name.capitalize())
# 7 将 name 变量对应的值变小写,并输出结果
print(name.lower())
# 8 请输出 name 变量对应的值的第 2 个字符?
print(name.strip()[1])
print(name[2])
# 9 请输出 name 变量对应的值的前 3 个字符?
print(name[:3])
# 10 请输出 name 变量对应的值的后 2 个字符?
print(name[-2:])
# 11 请输出 name 变量对应的值中 “e” 所在索引位置?
print(name.index('e'))
# 12 获取子序列,去掉最后一个字符。如: albert 则获取 alber
print(name[:-1])



# 练习二
data = ['albert', 18, [2000, 1, 2]]
data2 = []
for i in data:
    if isinstance(i, list):
        data2.extend(i)
    else:
        data2.append(i)
print(data2)
name, age, b_year, b_mon, b_day = data2
print(name, age, b_year, b_mon, b_day)



# 练习三
data = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90,]
dict1 = {'大于66的数':[], '小于66的数':[]}
for i in data:
    if i > 66:
        dict1['大于66的数'].append(i)
    elif i < 66:
        dict1['小于66的数'].append(i)
print(dict1)



# 练习四第一题
l = ['a', 'b', '1', 'a', 'a']
print(list(set(l)))



# 练习四第二题
l2 = []
for i in l:
    if i not in l2:
        l2.append(i)
    # else:      # 无需else
        # break  
print(l2)



# 练习四第三题
l = [
    {'name':'albert', 'age':18, 'sex':'male'},
    {'name':'james', 'age':35, 'sex':'male'},
    {'name':'taylor', 'age':25, 'sex':'female'},
    {'name':'albert', 'age':18, 'sex':'male'},
    {'name':'albert', 'age':18, 'sex':'male'},
]
k = []
for i in l:
    if i not in k:
        k.append(i)
    else:
        break
print(k)

# 练习四第三题参考答案一
s = set()
l1 = []
for item in l:
    val = (item['name'], item['age'], item['sex']) # ???
    if val not in s:
        s.add(val)
        l1.append(item)
print(l1)
print(s)

# 练习四第三题参考答案二：定义函数,既可以针对可以hash类型又可以针对不可hash类型
def func(items, key=None):
    s = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in s:
            s.add(val)
            yield item

print(list(func(l, key=lambda dic: (dic['name'], dic['age'], dic['sex']))))  # ???



# 练习五
s = 'hello albert albert say hello world'
from collections import Counter
cnt = Counter()
for i in s.split(' '):
    cnt[i] += 1
print(cnt)

dict2 = {}
for i in s.split(' '):
    dict2[i] = s.split(' ').count(i)
print(dict2)

# 练习五参考答案一
dict3 = {}
words = s.split()
for word in words:
    dict3.setdefault(word, s.count(word))  # ???
print(dict3)



# 练习六
goods_dict = {
    'apple':10,
    'mac':10000,
    'iphone':8000,
    'lenovo':3000,
    'chicken':10,
}
shop_dict = {}
i = 0
print('以下为本店所售商品及其单价，祝您购物愉快', goods_dict)
goon_flag = True if input("是否开始购物（是/否）？") == '是' else False
while goon_flag:
    goods_name = input("请输入您要购买的商品名称：")
    while goods_name not in goods_dict.keys():
        print("输入商品名有误，请重新输入")
        break
    else:
        goods_num = int(input("请输入您要购买%s的数量：" % goods_name))
        while not isinstance(goods_num, int): # 可用isdigit()
            print("输入商品数量有误，请重新输入")
            break
        else:
            i += 1
            key = '第'+str(i)+'件商品'
            shop_dict[key] = [goods_name, goods_dict[goods_name], goods_num]
            print('已加购%s %d件（%d元/件）' % (goods_name, goods_num, goods_dict[goods_name]))
            goon_flag = True if input("是否继续购物（是/否）？") == '是' else False
print(shop_dict)   

# 练习六参考答案一
msg_dic = {
    'apple': 10,
    'tesla': 1000000,
    'mac': 10000,
    'iphone': 8000,
    'chicken': 30,
    'pen': 3,
    'ruler': 5
}
goods_list = []
while True:
    for product, price in msg_dic.items():
        print('product: %s, price: %s' % (product, price))
    choice = input('please choose product>>:').strip()
    if choice == 'q':  # user can quit the program by inputting 'q'
        break
    elif choice not in msg_dic:
        print('The product you choose is invalid')
        continue
    else:
        while True:
            count = input('please input the number of the product>>:').strip()
            if not count.isdigit():
                print('The content you input is not number')
                continue
            else:
                goods_list.append((choice, msg_dic[choice], count))
                print(goods_list)
                break

