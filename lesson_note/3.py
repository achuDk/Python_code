# test = 'id\tname\tage\tgender\t\n1\ttom\t12\tf\n2\tjerry\t13\tm\n'
# v = test.expandtabs(10)
# print(v)

# test = "你是风儿我是沙"
# a = " "
# v = a.join(test)
# x = "*".join(v)
# print(test,'\n',v,'\n',x)

# #从右侧开始贪婪匹配去除字符
# test = "xaexlex"
# v = test.lstrip('abcdlefghighxea567')
# print(v)

# test = "jerry"
# v = test[0:len(test)]
# print(v)

# test = input(">>>")
# print(test)
# v = len(test)
# print(v)
#
# r = range(0,v)
# for i in r:
#     print(i,test[i])

test = input(">>>")
for i in range(0,len(test)):
    print(i,test[i])