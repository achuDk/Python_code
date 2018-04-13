# name = "aleX"
# a = name.strip()
# print(a)
# b = name.startswith("al")
# print(b)
# c = name.endswith("X")
# print(c)
# d = name.replace("l","p")
# print(d)
# e = name.split("l")
# print(e)
# f = "列表"
# print(f)
# g = name.upper()
# print(g)
# h = name.lower()
# print(h)
# i = name[1]
# print(i)
# j = name[2]
# print(j)
# k = name[-2:]
# print(k)
# l = name.index("e")
# print(l)
# m = name[0:-1]
# test1 = "oldboy"
# n = test1[0:-1]
# test2 = "root"
# o = test2[0:-1]
# print(m,n,o)

# li = "alexericrain"
# v = "_".join(li)
# print(v)
# li = ["alex","eric","rain"]
# v = "".join(li)
# print(v)

# express = input("请输入计算式：\n")
# x = express.split("+")
# print(x)
# y = int(x[0])+int(x[1])
# print(y)

# while True:
#     string = input("请输入内容(字母和数字)：\n")
#     if string.isalnum() == True:
#         x = 0
#         y = 0
#         for i in range(len(string)):
# #            print(i)
#             j = string[i]
#             if j.isdecimal() == True:
#                 x += 1
#             else:
#                 y += 1
#         print("数字个数:",x,"\n","字母个数:",y)
#     else:
#         print("输入不规范，请重新输入。")
#         continue

# test = "{0}最喜欢在{2}{1}"
# v = test.format(input("名字:"),input("爱好:"),input("地点:"))
# print(v)

import random
i = 0
while True:
    i += 1
    if i < 4:
        m = random.randrange(1000,9999)
#        print(m,type(m))
        n = int(input("请输入所示验证码：\n"))
#        print(n,type(n))
        if m == n:
            print("验证码通过。")
            break
        else:
            print("验证码错误，请重新输入。")
            continue
    else:
        print("次数过多，请稍后再试。")
        break

