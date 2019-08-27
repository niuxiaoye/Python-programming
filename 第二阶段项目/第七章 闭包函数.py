# 内部函数对外部函数作用域里变量的引用(非全局变量)则称内部函数为闭包

"""
理解闭包函数的作用一：提高代码可复用性

"""
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of # 返回值是 exponent_of 函数
square = nth_power(2) # 计算一个数的平方
cube = nth_power(3) # 计算一个数的立方
print(square(2))  # 计算 2 的平方
print(cube(2)) # 计算 2 的立方



"""
理解闭包函数的作用二：装饰器
开放封闭原则：已经实现的代码不允许被修改，但可以被扩展
装饰器的功能主要有：
    1. 引入日志
    2. 函数执行时间统计
    3. 执行函数前预备处理
    4. 执行函数后清理功能
    5. 权限校验等场景应用
    6. 缓存
    
"""
#定义函数：完成数据包裹
def makeBold(fn):
    def wrapped():
        return "<b>"+fn()+"</b>"
    return wrapped

#定义函数：完成数据包裹
def makeItalic(fn):
    def wrapped():
        return "<i>"+fn()+"</i>"
    return wrapped

'''
@makeBold后会进行以下操作：
    1. 执行makeBold函数，并将@makeBold下面的函数test1作为makeBold函数的参数
    2. 将执行完的@makeBold函数返回值赋值给@makeBold下面的函数test1，得到新的test1
    
'''
@makeBold
def test1():
    return "hello world-1"

@makeItalic
def test2():
    return "hello world-2"

'''
先执行makeItalic，再执行makeBold
'''
@makeBold
@makeItalic
def test3():
    return "hello world-3"

print(test1())
print(test2())
print(test3())



"""
练习一

编写装饰器：为多个函数加上认证的功能（用户的账号密码来源于文件）
要求：登陆成功一次，后续的函数都无需再输入用户名和密码；
注意：从文件中读出字符串形式的代码，可以用以下方式把字典字符串转化成字符串
    eval('{"name":"albert", "password":"123"}')
    
"""
def auth(func):
    def wrapper():
        with open("用户信息.txt", "r", encoding="utf-8") as f:
            user_info_dict = {}
            user_info = f.read().split('|')
            for i in range(0, len(user_info), 3):
                user_info_dict[user_info[i]] = [user_info[i+1], int(user_info[i+2])]
        user_name = input('请输入用户名：')
        password = input('请输入密码：')
        if user_name in user_info_dict and password == user_info_dict[user_name][0]:
            func()
        else:
            print('用户名或密码错误')
    return wrapper

@auth
def log_in():
    print('登陆成功')

@auth    # 没有实现登陆一次后其他操作无需登陆的功能
def change_password():
    print('可以修改密码了')

@auth  
def shopping():
    print('可以开始购物了')

log_in()
change_password()
shopping()

# 练习一参考答案
db = 'a.txt'
login_status = {'status': False}


def auth(auth_type='file'):
    def auth2(func):
        def wrapper(*args, **kwargs):
            if login_status['status']:  # 这样解决上面的登陆一次无需验证问题
                return func(*args, **kwargs)
            if auth_type == 'file':
                with open(db, encoding='utf-8') as f:
                    dic = eval(f.read())
                name = input('username: ').strip()
                password = input('password: ').strip()
                if name == dic['name'] and password == dic['password']:
                    login_status['status'] = True
                    return func(*args, **kwargs)
                else:
                    print('username or password error')
            elif auth_type == 'sql':
                pass
            else:
                pass

        return wrapper

    return auth2

@auth()
def index():
    print('index')

@auth(auth_type='file')
def home(name):
    print('welcome %s to home' % name)


index()
home('albert')



"""
练习二

编写装饰器：为多个函数加上认证功能
要求：登陆成功一次，在超时时间内无需重复登陆，超过了超时时间，则必须重新登录

"""
import time

login_status = {'status': False}
last_login = time.time()

def auth(func):
    def wrapper(*args, **kwargs):
        global last_login
        if login_status['status'] and time.time() - last_login <= 30:
            return func(*args, **kwargs)
        with open("用户信息.txt", "r", encoding="utf-8") as f:
            user_info_dict = {}
            user_info = f.read().split('|')
            for i in range(0, len(user_info), 3):
                user_info_dict[user_info[i]] = [user_info[i+1], int(user_info[i+2])]
        user_name = input('请输入用户名：')
        password = input('请输入密码：')
        if user_name in user_info_dict and password == user_info_dict[user_name][0]:
            last_login = time.time()
            login_status['status'] = True
            return func(*args, **kwargs)
        else:
            print('用户名或密码错误')
    return wrapper

@auth
def log_in():
    print('登陆成功')

@auth    # 没有实现登陆一次后其他操作无需登陆的功能
def change_password():
    print('可以修改密码了')

@auth  
def shopping():
    print('可以开始购物了')

log_in()
time.sleep(31)
change_password()
shopping()

# 练习二参考答案
import time
import random

user_data = {
    'user': None,
    'login': False,
    'now_time': time.time()
}
db_username = 'albert'
db_password = '123'

def auth(func):
    def wrapper(*args, **kwargs):
        passed_time = time.time() - user_data['now_time']

        if user_data['user'] and passed_time < 3:
            return func(*args, **kwargs)
        else:
            while True:
                username = input('input your username>>:').strip()
                password = input('input your password>>:').strip()
                if username == db_username and password == db_password:
                    print('login successfully')
                    user_data['user'] = username
                    user_data['login'] = True
                    user_data['now_time'] = time.time()
                    return func(*args, **kwargs)
                else:
                    print('username or password is invalid')

    return wrapper

@auth
def index():
    print('This is index page')

@auth
def home(name):
    print('Welcome %s to home page' % name)

index()
time.sleep(random.randint(2, 4))  # create 2-4 random number
home('albert')



"""
练习三

编写日志装饰器：一旦某函数执行，则将函数执行时间写入到日志文件中，日志文件路径可以指定
注意：时间格式都获取

"""
import datetime

def log(func):
    def wrapper():  # 日志路径指定没有实现
        func()
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(str(datetime.datetime.now())+'\n')
    return wrapper

@log
def func1():
    print('hello world!')

func1()

# 练习三参考答案
import time

def add_log(file):
    def wrapper(func):
        def inner(*args, **kwargs):
            with open(file, 'a', encoding='utf-8') as f:
                f.write('[%s]:[%s]\n' % (func.__name__, time.strftime('%Y-%m-%d %X')))
                return func(*args, **kwargs)

        return inner

    return wrapper

@add_log('db1.txt')
def index():
    print('This is index page')

@add_log('db2.txt')
def home(name):
    print('Welcome %s to home page' % name)

index()
home('albert')
