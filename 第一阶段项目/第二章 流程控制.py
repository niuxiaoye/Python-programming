import getpass
import time



'''
练习一：
    写一个用户登陆认证的程序，请用户分别输入用户名和密码来认证。
'''
my_username = 'Molly'
my_password = 'BeautifulMolly'
input_times = 0
while True:
    input_name = input("请输入您的用户名：")
    input_pswd = getpass.getpass("请输入您的密码：")
    input_times += 1
    if input_name == my_username and input_pswd == my_password and input_times <= 3:
        print("验证通过")
        break
    elif input_times < 3:
        print("用户名或密码错误，请重新输入。您还可输入%d次" % (3-input_times))        
    else:
        print("用户名或密码错误，您今日可输入次数已用尽，请明日再试")
        break



'''
练习二：
    写一个打印用户权限的程序，请用户输入用户名来验证。
    molly --> 超级管理员
    tom --> 普通管理员
    jack, rain --> 业务主管
    其他 --> 普通用户
'''
initial_role  = {"molly":"超级管理员", "tom":"普通管理员", "jack":"业务主管", 
                    "rain":"业务主管", "其他":"普通用户"}
initial_acss = {"超级管理员":["建表","删表","修改","查找"],
                    "普通管理员":["建表","修改","查找"],
                    "业务主管":["建表","查找"],
                    "普通用户":["查找"]}
find_flag = True
your_name = input("请输入您的用户名：")
while find_flag:
    for k1, v1 in initial_role.items():
        if your_name == k1:
            for k2, v2 in initial_acss.items():
                if v1 == k2:
                    print("你的权限包括：", v2)
                    find_flag = False
    else:
        your_name = '其他'



'''
练习三：
    写一个根据当日日期来说明是否上班的程序，请用户输入日期来获取
'''
initial_agenda = {"Mon":"假期综合症，调整心情ing", 
                        "Tue":"绝望得等待放假ing", 
                        "Wed":"象征性干点活儿ing", 
                        "Thu":"快要坚持不下去...", 
                        "Fri":"假期倒计时！", 
                        "Sat":"假期第一天，休息ing", 
                        "Sun":"抓紧时间浪～"}
for k, v in initial_agenda.items():
    if time.strftime("%a", time.localtime()) == k:
        print(v)
        break



'''
练习四：
    写一个循环验证用户登陆的程序，用户认证登陆成功后，输入‘q'退出程序，
    用户认证失败后重复让用户执行登陆操作，
    当用户重复次数超过3次仍没有登陆成功，则退出程序。
'''
my_username = 'Molly'
my_password = 'BeautifulMolly'
input_times = 0
input_text = ''
while True:
    input_name = input("请输入您的用户名：")
    input_pswd = getpass.getpass("请输入您的密码：")
    input_times += 1
    if input_name == my_username and input_pswd == my_password and input_times <= 3:
        print("验证通过")
        while input_text != 'q':
            input_text = input("开始写代码吧：")
        print("拜拜～")
        break
    elif input_times < 3:
        print("用户名或密码错误，请重新输入。您还可输入%d次" % (3-input_times))        
    else:
        print("用户名或密码错误，您今日可输入次数已用尽，请明日再试")
        break
    
# 练习四参考答案一：
name = 'Albert'
password = '123'
while True:
    inp_name = input('用户名: ')
    inp_pwd = input('密码: ')
    if inp_name == name and inp_pwd == password:
        while True:
            cmd = input('>>: ')
            if not cmd: continue #如果为空则重新输入
            if cmd == 'quit':    #上一个if没有else，则顺序执行下一个if
                break
            print('run <%s>' % cmd)
    else:
        print('用户名或密码错误')
        continue
    break
    
# 练习四参考答案二：使用tag
name = 'Albert'
password = '123'
tag = True
while tag:
    inp_name = input('用户名: ')
    inp_pwd = input('密码: ')
    if inp_name == name and inp_pwd == password:
        while tag:
            cmd = input('>>: ')
            if not cmd: continue
            if cmd == 'quit':
                tag = False
                continue
            print('run <%s>' % cmd)
    else:
        print('用户名或密码错误')


'''
练习五：
    写一个用户猜年龄的游戏，允许用户最多尝试3次，
    每尝试3次后，如果还没猜对，就问用户是否还想继续玩，
    如果回答Y或y，就继续让其猜3次，
    如果回答N或n，就退出程序，
    如果猜对了，就直接退出。
'''
my_age = 26
guess_times = 0
end_flag = True
while end_flag:
    your_guess = int(input("你猜我的年龄是："))
    guess_times += 1
    if my_age < your_guess and guess_times < 3:
        print("我看起来这么沧桑吗？")
    elif my_age > your_guess and guess_times < 3:
        print("我看起来这么年轻吗？")
    elif my_age != your_guess and guess_times == 3:
        goon_flag = input("次数用完了，还没猜对。要再试试吗？")
        if goon_flag == 'Y' or goon_flag == 'y':
            guess_times = 0
        elif goon_flag == 'N' or goon_flag == 'n':
            print("这么快就放弃了，友尽！")
            end_flag = False
    else:
        print("猜对了！友谊地久天长～")
        break

# 练习五参考答案一
Albert_age = 18
count = 0
while True:
    if count == 3:   # 将是否达到3次和是否猜对拆成了两个if语句来写。
        choice = input('继续(Y/N?)>>: ')
        if choice == 'Y' or choice == 'y':
            count = 0
        else:
            break
    guess = int(input('>>: '))
    if guess == Albert_age: # 只有<3的情况下才能执行这个if语句
        print('you got it')
        break
    count += 1

'''
练习六：
    按要求打印如下结果
'''
# 1. 使用while循环输出1 2 3 4 5 6 7 8 9 10
i = 1
while i <= 10:
    print(i)
    i += 1
    
# 2. 求1-100的所有数的和
sum_ = 0
for i in range(101):
    sum_ += i
print("1-100的所有数的和为：%d" % sum_)

# 3. 输出1-100内所有的奇数
for i in range(1, 101, 2):
    print(i)
    
# 4. 输出1-100内所有的偶数
for i in range(2, 101, 2):
    print(i)
    
# 5. 求1-2+3-4+5...99的所有数的和
sum_ = 0
j = 0
for i in range(1, 100, 2):
    sum_ = sum_ + i + j
    j = (i + 1) * (-1)
print(sum_)


'''
练习七：
    打印金字塔图形（等腰三角形），上面一行内容永远比下面少两颗星星
    且位于下面一行的正下方（用两层for loop）
'''
i = 5
for num in range(1, i*2, 2):
    print(('*'*num).center(i*2, ' '))

# 练习七参考答案一
"""
分析
#max_level=5
    *        #current_level=1，空格数=4，*号数=1
   ***       #current_level=2,空格数=3,*号数=3
  *****      #current_level=3,空格数=2,*号数=5
 *******     #current_level=4,空格数=1,*号数=7
*********    #current_level=5,空格数=0,*号数=9
#数学表达式
空格数=max_level-current_level
*号数=2*current_level-1
"""
max_level = 5
for current_level in range(1, max_level + 1):
    for i in range(max_level - current_level):
        print(' ', end='')  # 在一行中连续打印多个空格
    for j in range(2 * current_level - 1):
        print('*', end='')  # 在一行中连续打印多个空格
    print()