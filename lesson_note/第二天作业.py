# 1：编写for循环，利用索引遍历出每一个字符
# msg = "hello egon 666"
# for i in msg:
#     print(i)
# msg1 = input(">>>")
# for i in msg1:
#     print(i)
# 2：编写while循环，利用索引遍历出每一个字符
# i = 0
# msg='hello egon 666'
# while i < len(msg):
#     print(i,msg[i])
#     i += 1

# 4：将该字符的文件名，文件大小，操作方法切割出来
# msg='/etc/a.txt|365|get'

# v1,v2,v3 = msg.split("|")
# print(v1,"\n",v2,"\n",v3)
# ll = msg.split("|")
# print(ll[0])
# print(ll[1])
# print(ll[2])

# 8.
# 1.
# 两层while循环，外层的while循环，让用户输入用户名、密码、工作了几个月、每月的工资（整数），用户名或密码为空，或者工作的月数不为整数，或者
# 月工资不为整数，则重新输入
# 2.
# 认证成功，进入下一层while循环，打印命令提示，有查询总工资，查询用户身份（如果用户名为alex则打印super
# user，如果用户名为yuanhao或者wupeiqi
# 则打印normal
# user，其余情况均打印unkown
# user），退出功能
# 3.
# 要求用户输入退出，则退出所有循环（使用tag的方式）
#
#
# 运行效果如下：
# user: egon
# password: 123
# work_mons: 12
# salary: 10000
#
# 1
# 查询总工资
# 2
# 查询用户身份
# 3
# 退出登录
#
# >>: 1
# 总工资是: 120000.0
#
# 1
# 查询总工资
# 2
# 查询用户身份
# 3
# 退出登录
#
# >>: 2
# unkown
# user
#
# 1
# 查询总工资
# 2
# 查询用户身份
# 3
# 退出登录
#
# >>: 3

# i = 0
# while i < 3:
#     username = input("Username >>> ")
#     passwd = input("Password >>> ")
#     month = input("How long you work >>> ")
#     salary = input("How many you earn per month >>> ")
#     if username.isspace() == True or passwd.isspace() == True or month.isdigit() == False or salary.isdigit() == False:
#         print("Wrong input,please input again !")
#         i += 1
#         print("Attention ! Remain ",3-i," retry times.")
#         continue
#     else:
#         print("Login successful !")
#         while True:
#             query = input("1 >> Wage query\n2 >> Role query\n3 >> Quit\nMake choice : ")
#             # print(type(query))
#             if query == "1":
#                 print("Total Wage : ",int(month)*int(salary))
#             elif query  == "2":
#                 if username == "alex":
#                     print("Super user")
#                 elif username == "seven" or username == "eagon":
#                     print("Normal user")
#                 else:
#                     print("Stranger")
#             elif query == "3":
#                 break
#     stop = input("Type quit or exit to stop or to continue.\n >>> ")
#     if stop == "quit" or stop == "exit":
#         break
#     else:
#         continue

# 一、元素分类
# 有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
# 即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}

# 方法一：
#     li = [11,22,33,44,55,66,77,88,99,90]
#     i = 0
#     child = []
#     dic1 = []
#     dic2 = []
#     for i in li:
#         # print(i,type(i))
#         if i < 66:
#             dic1.append(i)
#         elif i >= 66:
#             dic2.append(i)
#     print("dic1:",dic1,"\ndic2:",dic2)

# 方法二：
#     while i < len(li):
#         child.append(li[i])
#         # print(i,child,child[i])
#         if child[i] > 66:
#             dic1.append(child[i])
#         elif child[i] <= 66:
#             dic2.append(child[i])
#         i += 1
#     print("dic1:",dic1,"\ndic2:",dic2)

# 二、查找
# 查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。
# li = ["alec", " aric", "Alex", "Tony", "rain"]
# tu = ("alec", " aric", "Alex", "Tony", "rain")
# dic = {'k1': "alex", 'k2': ' aric',  "k3": "Alex", "k4": "Tony"}
#
# child = []
# for i in li:
#     # print(i,type(i))
#     child.append(i.strip())
# print(i,child)

# 三、输出商品列表，用户输入序号，显示用户选中的商品
# li = ["手机", "电脑", '鼠标垫', '游艇']
# for i in li:
#     print(li.index(i),i)
# while True:
#     j = input("请输入编号，选择对应商品：>>>")
#     if j.isdigit() and int(j) < len(li):
#         print(j,li[int(j)])
#     else:
#         print("输入错误，请重新输入")
#         continue

# 四、购物车
# 功能要求：
# 要求用户输入总资产，例如：2000
# 显示商品列表，让用户根据序号选择商品，加入购物车
# 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
# 附加：可充值、某商品移除购物车
# goods = [{"name": "电脑", "price": 1999},{"name": "鼠标", "price": 10},{"name": "游艇", "price": 20},{"name": "美女", "price": 998}]
# money = input("输入总资产：")
# while True:
#     print("商品编号  商品名称  价钱")
#     for i in goods:
#         print("  ",goods.index(i),"    ",i["name"], "  ",i["price"])
#     cart = []
#     price = []
#     while True:
#         j = input("选择加入购物车的商品：")
#         if j.isdigit() and int(j) < len(goods):
#             cart.append(goods[int(j)]["name"])
#             price.append(goods[int(j)]["price"])
#             money = int(money) - goods[int(j)]["price"]
#             while int(money) < 0:
#                 action = input("余额不足，请按 c 键充值(如要移除商品请按 d 键)")
#                 if action == "d":
#                     x = -1
#                     for k in cart:
#                         x += 1
#                         print("购物车内商品、编号及价格：",x,k,price[cart.index(k)])
#                     l = input("选择删除的商品编号：")
#                     drop_goods = cart.pop(int(l))
#                     drop_price = price.pop(int(l))
#                     money = int(money) + drop_price
#                     break
#                 else:
#                     pass
#                 charge = input("请输入充值金额：")
#                 money = int(money) + int(charge)
#                 print("当前余额：",money)
#                 continue
#             while int(money) > 0:
#                 print("购物车包含：", cart)
#                 # print("价格记录：",price)
#                 print("余额：", money)
#                 break
#         else:
#             print("无此编号，重新输入")
#             continue

# 选做题：用户交互，显示省市县多级联动的选择
#
# dic = {
#     "河北":{
#         "石家庄":{"鹿泉":{}, "藁城":{}, "元氏":{}},
#         "邯郸":{"永年":{}, "涉县":{}, "磁县":{}},
#     },
#     "河南":{},
#     "山西":{},
# }
# print(dic)
# path = []
# while True:
#     temp = dic
#     for i in path:
#         temp = temp[i]
#     print("当前节点的所有子节点：",list(temp.keys()))
#     j = input("1：查看当前节点的子节点；2：添加节点；b：返回上一级；q：退出>>>")
#     if j == "1":
#         name = input("请输入要查看的节点名：")
#         path.append(name)
#     elif j == "2":
#         k = input("请输入要添加的节点：")
#         temp[k] = {}
#     elif j == "b":
#         if path:
#             path.pop()
#     elif j == "q":
#         break
#     else:
#         print("输入错误，请重新输入！")








#实现增、删、改、查的功能
# dic = {
# 	"植物":
# 		{"草本植物":
# 			["牵牛花","瓜叶菊","葫芦","翠菊","冬小麦","甜菜"],
# 		"木本植物":
# 			["乔木","灌木","半灌木","如松","杉","樟"],
# 		"水生植物":
# 			["荷花","千屈菜","菖蒲","黄菖蒲","水葱","再力花","梭鱼草"]},
# 	"动物":
# 		{"两栖动物":
# 			["山龟","山鳌","石蛙","娃娃鱼","蟾蜍","龟","鳄鱼","蜥蜴","蛇"],
# 		"禽类":
# 			["雉鸡","原鸡","长鸣鸡","昌国鸡","斗鸡","长尾鸡","乌骨鸡"],
# 		"哺乳类动物":
# 			["虎","狼","鼠","鹿","貂","猴","树懒","斑马","狗","貘"]},
#     "水里游的":
#         {"青蛙"}
# }
#
# while True:
#     print(dic)
#     list = []
#     for i,v in enumerate(dic,1):
#         print(i,v)
#         list.append(v)
#         # print(list)
#     print(" 插入条目".ljust(20, "."), "按 i 键;\n",
#           "删除条目".ljust(20, "."), "按 d 键;\n",
#           "修改条目".ljust(20, "."), "按 m 键;\n",
#           "查看条目".ljust(20, "."), "按对应数字键")
#     first = input("输入选择结果：")
#     if first.isalpha() == True and first == "i":
#         while
#         ikey = input("请输入要增加的类名：")
#         dic[ikey] = {}
#         ikey_1 = input("请输入要增加的子类名：")
#         dic[ikey][ikey_1] = []
#
#         # print(dic)
#         continue
#     elif first.isalpha() == 1 and first == "d":
#         dkey = input("请输入要删除的类名：")
#         dic.pop(dkey)
#         continue
#     elif first.isalpha() == 1 and first == "m":
#         mkey = input("请输入要修改的类名：")
#         if mkey in dic.keys():
#             newkey = input("请输入修改后的类名：")
#             x = dic.get(mkey)
#             dic.pop(mkey)
#             dic.setdefault(newkey,x)
#         else:
#             print("输入错误，重新输入。")
#             continue
#         # print(dic)
#         continue
#     elif first.isdigit() == True:
#         test = []
#         for j,k in enumerate(dic[list[int(first)-1]],1):
#             print(j,k)
#             test.append(k)
#         print("插入条目".ljust(20, "."), "按 i 键;\n",
#               "删除条目".ljust(20, "."), "按 d 键;\n",
#               "修改条目".ljust(20, "."), "按 m 键;\n",
#               "返回上层".ljust(20, "."), "按 r 键;\n",
#               "查看条目".ljust(20, "."), "按对应数字键")
#         second = input("输入选择结果：")
#         for l,m in enumerate(dic[list[int(first)-1]][test[int(second)-1]],1):
#             print(l,m)
#         print("插入条目".ljust(20, "."), "按 i 键;\n",
#               "删除条目".ljust(20, "."), "按 d 键;\n",
#               "修改条目".ljust(20, "."), "按 m 键;\n",
#               "返回上层".ljust(20, "."), "按 r 键;\n")
#     else:
#         print("输入不合法，请重新输入。")
#         continue

#实现返回上一层的功能
#实现增、删、改、查的功能

dic = {
    "语文":{
        "古文":{"大学":{},"论语":{}},
        "诗词歌赋":{"唐诗":{},"宋词":{},"元曲":{}},
    },
    "数学":{
        "几何":{},
        "高数":{},
    },
    "历史":{
        "近代史":{},
        "现代史":{},
    },
}

path = []
while True:
    li = []
    cache = dic
    for i in path:
        cache = cache[i]
    li = list(cache.keys())
    print("当前节点的所有子节点编号及名称：")
    for k in li:
        print(li.index(k)+1,k)
    j = input("i:增加节点；d:删除节点；m:修改节点;f:查询；b:返回上一层;q:退出;>>>")
    if j == "i":
        name = input("输入要增加的节点名称：")
        if name:
            cache[name] = {}
        else:
            print("增加的节点名称不能为空！")
    elif j == "d":
        number = input("输入要删除节点的编号：")
        if number.isdigit() == True and int(number) > 0 and int(number) <= len(li):
            if cache:
                cache.pop(li[int(number) - 1])
        else:
            print("输入超出范围或非数字！")
    elif j == "m":
        number = input("输入要进入或查看节点的编号：")
        if number.isdigit() == True and int(number) > 0 and int(number) <= len(li):
            temp = cache.get(li[int(number)-1])
            modify = input("请输入修改后的名字：")
            if modify and modify not in cache:
                cache.pop(li[int(number)-1])
                cache.setdefault(modify,temp)
            else:
                print("修改后的名称不准为空，且不能重名！")
        else:
            print("输入超出范围或非数字！")
    elif j == "f":
        number = input("输入要进入或查看节点的编号：")
        if number.isdigit() == True and int(number) > 0 and  int(number) <= len(li):
            path.append(li[int(number)-1])
        else:
            print("输入超出范围或非数字！")
    elif j == "b":
        if path:
            path.pop()
    elif j == "q":
        new_dic = dic
        print("操作结果:", new_dic)
        break
    else:
        print("输入错误，请重新输入！")