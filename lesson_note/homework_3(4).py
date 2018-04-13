#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
四、购物车
功能要求：

要求用户输入总资产，例如：2000
显示商品列表，让用户根据序号选择商品，加入购物车
购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
附加：可充值、某商品移除购物车
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
'''
goods = [{'name':'电脑','price':1999},{'name':'鼠标','price':10},{'name':'游艇','price':20},{'name':'美女','price':998}]

#用户输入初始金额----------------------------
while True:
    money = input('请输入您的总资产： ').strip()
    if money.isdigit():                   # 负数返回False
        money = int(money)
        if money > 0 :
            break
        else:
            print('本商店恕不赊账')
    else:
        print('请输入整数！')

#打印商品列表--------------------------------
print ('商品列表如下：')
count = 1
for i in goods:
    print ('%s:%s  %s' %(count,i['name'],i['price']))
    count += 1
good_list = []              #定义购物车列表
time = 1                    #第一次默认直接进入购物选项，之后给用户提供其他操作选项

#用户开始购物-------------------------------
while True:
    if time >= 2:
        choice = input('1.继续购物 2.结账 3.充值 4.移除购物车商品 5.退出\n>>:  ')
        if choice == '1':
            pass
        elif choice == '2':
            cost = 0
            for k in good_list:
                cost += k['price']
            if money >= cost:
                print ('购买成功')
                print ('您的余额还有%s' %(money-cost))
                break
            else:
                print ('余额不足')
                continue
        elif choice == '3':
            money_add = input('请输入充值金额： ')
            if money_add.isdigit():
                money_add = int(money_add)
            else:
                print('输入错误')
                continue
            money += money_add
            print('您的余额还有%s' % money )
            continue
        elif choice == '4':
            count1 = 1
            for n in good_list:
                print ('%s: %s' %(count1,good_list[count1-1]['name']))
                count1 += 1
            moveaway = input('请输入要移除的商品的序号： ')
            if moveaway.isdigit():
                moveaway = int(moveaway)
                if 1 <= moveaway <= len(good_list):
                    good_list.pop(moveaway-1)
                else:
                    print('输入有误')
                    continue
            else:
                print('输入有误')
                continue
            if len(good_list) > 0:
                print('您的购物车中有 ', end='')
                for j in good_list:
                    print(j['name'], end=' ')
                print()
            continue
        elif choice == '5':
            break
        else:
            print('输入有误，请重新输入 ')
            continue
    sum = input('请输入您选中商品的序号： ')
    if sum.isdigit():
        sum = int(sum)
        if 1 <= sum <= len(goods):
            print ('您选中了%s' %goods[sum-1]['name'])
            time += 1
            good_list.append(goods[sum-1])
            print('您的购物车中有 ',end = '')
            for j in good_list:
                print (j['name'],end = ' ')
            print()
        else:
            print ('请输入%s以内的正数' %len(goods))
    else:
        print ('请输入%s以内的正数' %len(goods))
