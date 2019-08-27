'''
练习一

写函数：用户传入修改的文件名，与要修改的内容，执行函数，完成批量修改操作
'''
def to_modify_doc(doc_name, doc_content):
    with open(doc_name, 'w+', encoding = 'UTF=8') as f:
        f.write(doc_content)
        
to_modify_doc('第六章.txt', '改成这些')

# 练习一参考答案一
import os

def modify_file(file_name, old_content, new_content):
    with open(file_name, mode='rt', encoding='utf-8') as read_f, \
            open('%s.swap' % file_name, mode='wt', encoding='utf-8') as write_f:
        for line in read_f:
            if old_content in line:
                line = line.replace(old_content, new_content)

            write_f.write(line)

    os.remove(file_name)
    os.rename('%s.swap' % file_name, file_name)

modify_file('db.txt', '马一特', '马一特[Albert]')



'''
练习二

写函数：计算传入字符串中【数字】、【字母】、【空格】以及【其他】的个数
'''
def to_compute_num(str):
    num = 0
    alpha = 0
    space = 0
    else_c = 0    
    
    for i in str:
        if i.isdigit():
            num += 1
        elif i.isalpha():
            alpha += 1
        elif i == ' ':
            space += 1
        else:
            else_c += 1
            
    return {'数字个数':num, '字母个数':alpha, '空格个数':space, '其他字符个数':else_c}

to_compute_num('as d  fkh13 8469@#$^%^&*')



'''
练习三

写函数：判断用户传入的对象（字符串、列表、元组）长度是否大于5
'''
def to_judge_length(objecto):
    flag = False
    if len(objecto) > 5:
        flag = True
    else:
        flag = False       
    return flag

print(to_judge_length('aewfgarg'))
print(to_judge_length([3,5,7,9,]))
print(to_judge_length((5,8,0,3,5,)))

# 练习三参考答案
def judge_length(data):
    if len(data) > 5:
        return True
    else:
        return False



'''
练习四

写函数：检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
'''
def to_first_two(objectc):
    if len(objectc) > 2:
        first_two = objectc[:2]
    else:
        first_two = objectc
    return first_two

print(to_first_two([3,6,8,4,2,]))
print(to_first_two([4,6]))



'''
练习五

写函数：检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
'''
def to_odd(objectc):
    l = []
    for i in range(0, len(objectc), 2):
        l.append(objectc[i])
    return l

print(to_odd([1,3546,78,245,124,678,789,346,1,34]))
print(to_odd((245,45,89,234,67,879,)))



'''
练习六

写函数：检查字典的每一个value的长度，如果大于2，那么保留前两个长度的内容，并将新内容返回给调用者。
'''
def first_two(objectc):
    for i in objectc.keys():
        if len(objectc[i]) > 2:
            objectc[i] = objectc[i][:2]
    return objectc

print(first_two({'a1':'wefserg', 'a2':(1,2), 'a3':[7,5,3,8,2,]}))

# 练习六参考答案
def check_up_list(data_dict):
    for key, value in data_dict.items():
        if len(value) > 2:
            data_dict[key] = value[:2]
    return data_dict



'''
练习七

用函数改写第一阶段购物项目
'''
import getpass
from prettytable import PrettyTable

def  to_registered():
    print('----------------------------------------')
    print('您正在注册成为本站用户')
    print('----------------------------------------')
    cust_name = input('请输入您的用户名：')
    cust_password = getpass.getpass('请输入您的密码：')
    cust_pass_vrfy = getpass.getpass('请再次输入您的密码：')
    cust_income = int(input('请输入您的工资：'))
    if cust_password == cust_pass_vrfy:
        with open("用户信息.txt", "a+", encoding="utf-8") as f:
            new_user = '|' + cust_name + '|' + cust_password + '|' + str(cust_income)
            f.write(new_user)
        global cust_flag 
        cust_flag = True
        print('您已注册成功，登陆后即可开始购物')
    else:
        print('两次输入的密码不一致，请重新输入')

        
def import_information():
    with open("黑名单客户.txt", "r", encoding="utf-8") as f:
        black_user = f.read().split('|')
    with open("用户信息.txt", "r", encoding="utf-8") as f:
        user_info_dict = {}
        user_info = f.read().split('|')
        for i in range(0, len(user_info), 3):
            user_info_dict[user_info[i]] = [user_info[i+1], int(user_info[i+2])]
    with open("商品编号.txt", "r", encoding="utf-8") as f:
        merchant_num_dict = {}
        merchant_num = f.read().split('|')
        for i in range(0, len(merchant_num), 2):
            merchant_num_dict[merchant_num[i]] = merchant_num[i+1]
    with open("商品价格.txt", "r", encoding="utf-8") as f:
        merchant_price_dict = {}
        merchant_price = f.read().split('|')
        for i in range(0, len(merchant_price), 2):
            merchant_price_dict[merchant_price[i]] = int(merchant_price[i+1])
    return black_user, user_info_dict, merchant_num_dict, merchant_price_dict

               
def log_in():
    input_name = input("请输入您的用户名：")
    input_pswd = getpass.getpass("请输入您的密码：")
    global input_times
    input_times += 1
    if input_name not in black_user and input_name in user_info_dict and input_pswd == user_info_dict[input_name][0] and input_times < 3:
        print('----------------------------------------')
        print('尊敬的会员您好\n以下为本站所售商品及其单价\n输入商品名或商品编号均可进行选购\n祝您购物愉快')
        print('----------------------------------------')
        merchant_table = PrettyTable()
        merchant_table.add_column("商品编号", list(merchant_num_dict.keys()))
        merchant_table.add_column("商品名称", list(merchant_num_dict.values()))
        merchant_table.add_column("商品单价", list(merchant_price_dict.values()))
        print(merchant_table)
        print('----------------------------------------')
        global log_in_flag
        log_in_flag = True
        return input_name
    elif input_name in black_user and input_times < 3:
        print('该用户名不可用')
    elif not(input_name in user_info_dict and input_pswd == user_info_dict[input_name][0]) and input_times < 3:
        print("用户名或密码错误，请重新输入。您还可输入%d次" % (3-input_times)) 
    else:
        new_black_user = '|' + input_name
        with open("黑名单客户.txt", 'a', encoding="utf-8") as f:
            f.write(new_black_user)
        log_in_flag = True
        print("用户名或密码错误，您可尝试次数已用尽")     
    
def shopping():
    goods_name = input("请输入您要购买的商品名称/商品编号：")
    good_num = int(input("请输入您要购买的数量：" ))
    if (goods_name.isalpha()) and (goods_name in merchant_price_dict.keys()) and (merchant_price_dict[goods_name]*good_num<=user_info_dict[input_name][1]):               
        global i
        i += 1
        key = '第'+str(i)+'件商品'
        shop_dict[key] = [goods_name, good_num, merchant_price_dict[goods_name]*good_num]   
        user_info_dict[input_name][1] -= merchant_price_dict[goods_name]*good_num
        print('已加购%s %d件（%d元/件）' % (goods_name, good_num, merchant_price_dict[goods_name]))
        global goon_flag
        goon_flag = True if input("是否继续购物（是/否）？") == '是' else False
    elif (not goods_name.isalpha()) and (goods_name in merchant_num_dict) and (merchant_price_dict[merchant_num_dict[str(goods_name)]]*good_num<=user_info_dict[input_name][1]):
        i += 1
        key = '第'+str(i)+'件商品'
        shop_dict[key] = [merchant_num_dict[str(goods_name)], good_num, merchant_price_dict[merchant_num_dict[str(goods_name)]]*good_num]
        user_info_dict[input_name][1] -= merchant_price_dict[merchant_num_dict[str(goods_name)]]*good_num
        print('已加购%s %d件（%d元/件）' % (merchant_num_dict[str(goods_name)], good_num, merchant_price_dict[merchant_num_dict[str(goods_name)]]))
        goon_flag = True if input("是否继续购物（是/否）？") == '是' else False                  
    elif (goods_name not in merchant_price_dict and goods_name not in merchant_num_dict):
        print("输入商品名有误，请重新输入")
    else:
        print('余额不足，请重新选购')
        
        
while True:
    
    cust_flag = True if input("是否是本站注册用户（是/否）？") == '是' else False
    while not cust_flag :
        to_registered()
    
    black_user, user_info_dict, merchant_num_dict, merchant_price_dict = import_information()
    
    input_times = 0
    log_in_flag = False
    while not log_in_flag:
        input_name = log_in() 
        
    shop_dict = {}
    i = 0
    goon_flag = True if input("是否开始购物（是/否）？") == '是' else False
    while goon_flag:
        shopping()           
    else:
        print('已购商品：')
        print(shop_dict)
        print('账户余额：%d' % user_info_dict[input_name][1])
        break