account_list = [
    {'name': 'tom',   'passwd': '123', 'goods': ['fish', 'rat']},
    {'name': 'jerry', 'passwd': '456', 'goods': ['rice', 'oil']},
    {'name': 'hachi', 'passwd': '789', 'goods': ['bone', 'meat']},
]
current_account = {'name':None,'status':False,'goods':None}

def authentication(func):
    print('发现一个函数，准备开始装饰该函数')
    def wrapper(*args, **kwargs):
        x = -1
        if current_account['name'] and current_account['status'] and current_account['goods']:
            res = func(*args, **kwargs)
            return res
        name = input('请输入用户名 >>> ').strip()
        passwd = input('请输入密码   >>> ').strip()
        for i in account_list:
            x += 1
            if name == i['name'] and passwd == i['passwd']:
                print('login successful!')
                current_account['name'] = name
                current_account['status'] = True
                current_account['goods'] = i['goods']
                res = func(*args, **kwargs)
                return res
        else:
            print('用户名或密码错误，请重新登录！')
    return wrapper

@authentication
def index():
    print('欢迎来到index')
@authentication
def home():
    print('欢迎%s回家' %current_account['name'])
@authentication
def cart():
    print('您的购物车：%s' %current_account['goods'])

print('before-->',current_account)
index()
print('after-->',current_account)
home()
cart()


#
# name = 'tom'
# print(1,name)
# def test(var):
#     print(2,var)
#     name = 'jerry'
#     print(3,name)
# test(name)
# print(4,name)