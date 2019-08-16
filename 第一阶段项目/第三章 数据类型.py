# 练习一
name = ' alberT'
print(name.strip())
print(name.strip().find('al', 0, 2))
print(name.strip().find('T', -1))
print(name.strip().replace('l', 'p'))
print(name.strip().split('l'))
print(name.strip().capitalize())
print(name.strip().swapcase())
print(name.strip()[1])
print(name.strip()[0:3])
print(name.strip()[-2:])
print(name.index('e'))
print(name.strip()[:-1])



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
    else:
        break
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
        while not isinstance(goods_num, int):
            print("输入商品数量有误，请重新输入")
            break
        else:
            i += 1
            key = '第'+str(i)+'件商品'
            shop_dict[key] = [goods_name, goods_dict[goods_name], goods_num]
            print('已加购%s %d件（%d元/件）' % (goods_name, goods_num, goods_dict[goods_name]))
            goon_flag = True if input("是否继续购物（是/否）？") == '是' else False
print(shop_dict)   



