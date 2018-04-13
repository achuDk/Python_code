# 1：编写for循环，利用索引遍历出每一个字符
# test = "hello world."
# for i in test:
#     print(i)

# abc = input(">>>")
# print(len(abc))
# for i in range(len(abc)):
#     print(i,abc[i])

# 2：编写while循环，利用索引遍历出每一个字符
# test = "hello world."
# i=1
# while i < len(test):
#     print(i,test[i])
#     i += 1

#3：中的alex替换成SB
# msg='hello alex'
# v = msg.replace("alex","alex:SB")
# print(v)

# 4：将该字符的文件名，文件大小，操作方法切割出来
# msg='/etc/a.txt|365|get'
# v = msg.split("|")
# print("filename:",v[0],"\n","filesize:",v[1],"\n","method:",v[2])

# # 5.编写while循环，要求用户输入命令，如果命令为空，则继续输入
# while  True:
#     test = input("enter command:\n")
#     if test.isspace() == True:
#         input("enter command:\n")
#     else:
#         print("ok")
#         break

#6.编写while循环，让用户输入用户名和密码，如果用户为空或者数字，则重新输入
# while True:
#     test = input("enter username:\n")
#     if test.isnumeric() == True or test.isspace() == True:
#         continue
#     else:
#         input("enter password:\n")
#         print("ok")
#         break

# 7.编写while循环，让用户输入内容，判断输入的内容以alex开头的，则将该字符串加上_SB结尾
# while True:
#     test = input("enter some string :\n")
#     if test.startswith("alex") == True:
#         print(test+"_SB")
#         break

# 8.以下小题：
#     (1).两层while循环，外层的while循环，让用户输入用户名、密码、工作了几个月、每月的工资（整数），用户名或密码为空，或者工作的月数不为整数，或者
#       月工资不为整数，则重新输入
#     (2).认证成功，进入下一层while循环，打印命令提示，有查询总工资，查询用户身份（如果用户名为alex则打印super user，如果用户名为yuanhao或者wupeiqi
#       则打印normal user，其余情况均打印unkown user），退出功能
#     (3).要求用户输入退出，则退出所有循环（使用tag的方式）
while True:
    username = input("enter your username:\n")
    password = input("enter your password:\n")
    worktime = input("enter your worktime(month):\n")
    earn_money = input("earn money every month:\n")

    if username.isspace() == True or password.isspace() == True or worktime.isdigit() != True or earn_money.isdigit() != True:
        print("please enter right info.")
        continue
    else:
        print("OK")
        print("total earn money:", int(earn_money) * int(worktime))

        if username == "alex":
            print("super user")
        elif username == "yuanhao" or username == "wupeiqi":
            print("normal user")
        else:
            print("unknown user")

    test = input("wanna stop program ? you can type 'quit' or 'exit':")
    if test == "quit" or test == "exit":
        print("program close.")
        break
    else:
        continue