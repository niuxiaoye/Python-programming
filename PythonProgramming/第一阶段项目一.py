import getpass
user_info = {'albert':['albert123', 3000]}
black_user = []
goods_dict = {
    'apple':5,
    'pen':10,
    'banana':4,
    'iphone':8000,
}
goods_num = {
    '1':'apple', 
    '2':'pen', 
    '3':'banana',
    '4':'iphone',     
}
shop_dict = {}
i = 0
input_times = 0


cust_flag = True if input("是否是本站注册用户（是/否）？") == '是' else False
while not cust_flag :
    print('您正在注册成为本站用户')
    cust_name = input('请输入您的用户名：')
    cust_password = getpass.getpass('请输入您的密码：')
    cust_pass_vrfy = getpass.getpass('请再次输入您的密码：')
    cust_income = int(input('请输入您的工资：'))
    if cust_password == cust_pass_vrfy:
        user_info[cust_name] = [cust_password, cust_income]
        cust_flag = True
        print('您已注册成功，登陆后即可购物～')
    else:
        print('两次输入的密码不一致，请重新注册')
        continue
else:
    input_name = input("请输入您的用户名：")
    input_pswd = getpass.getpass("请输入您的密码：")
    input_times += 1
    if input_name not in black_user and input_name in user_info and input_pswd == user_info[input_name][0] and input_times <= 3:
        print('尊敬的会员您好\n以下为本站所售商品及其单价\n输入商品名或商品编号均可进行选购\n祝您购物愉快', goods_dict)
        goon_flag = True if input("是否开始购物（是/否）？") == '是' else False
        while goon_flag:
            goods_name = input("请输入您要购买的商品名称/商品编号：")
            good_num = int(input("请输入您要购买%s的数量：" % goods_name))
            i += 1
            key = '第'+str(i)+'件商品'
            if (goods_name.isalpha()) and (goods_name in goods_dict.keys()) and (goods_dict[goods_name]*good_num<=user_info[input_name][1]):               
                shop_dict[key] = [goods_name, good_num, goods_dict[goods_name]*good_num]
                user_info[input_name][1] -= goods_dict[goods_name]*good_num
                print('已加购%s %d件（%d元/件）' % (goods_name, good_num, goods_dict[goods_name]))
                goon_flag = True if input("是否继续购物（是/否）？") == '是' else False
            elif (not goods_name.isalpha()) and (goods_name in goods_num) and (goods_dict[goods_num[str(goods_name)]]*good_num<=user_info[input_name][1]):
                shop_dict[key] = [goods_num[str(goods_name)], good_num, goods_dict[goods_num[str(goods_name)]]*good_num]
                user_info[input_name][1] -= goods_dict[goods_num[str(goods_name)]]*good_num
                print('已加购%s %d件（%d元/件）' % (goods_num[str(goods_name)], good_num, goods_dict[goods_num[str(goods_name)]]))
                goon_flag = True if input("是否继续购物（是/否）？") == '是' else False                  
            elif (goods_name not in goods_dict and goods_name not in goods_num):
                print("输入商品名有误，请重新输入")
                continue
            else:
                print('余额不足，请重新选购')
                continue
        else:
            print('已购商品：')
            print(shop_dict)
            print('账户余额：%d' % user_info[input_name][1])
    elif input_name in black_user:
        print('该用户名不可用')
    elif input_times < 3:
        print("用户名或密码错误，请重新输入。您还可输入%d次" % (3-input_times))        
    else:
        black_user.append(input_name)
        print("用户名或密码错误，您可尝试次数已用尽")