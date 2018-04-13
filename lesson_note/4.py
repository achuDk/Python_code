# print(list(zip(('hello'),(1,2,3,4,5))))
#
# a = zip(('a','b','c','d'),(1,2,3,4))
# print(list(a))
#
# dic = {'name':'abc','age':18,'gender':'f'}
# print(dic)
# print(dic.keys())
# print(list(dic.keys()))
#
# b = zip((dic.keys()),(dic.values()))
# print(list(b))



# li = [1,2,3,[4,5,6,[7,8,9,[10,11,12]]]]
# test = []
# def traversal(array):
#     for i in array:
#         if isinstance(i,list):
#             return traversal(i)
#         else:
#             # print(i)
#             test.append(i)
#     return test
# print(traversal(li))

#简单取最大最小值
# li = [1,3,546,123,-1]
# print(max(li),min(li))

#取字典的最大最小值，并取出对应的key
dic = {'apple':18,'banana':12,'pear':29}
# print(max(dic),max(dic.keys()),'\n',max(dic.values()))
print(max(zip(dic.values(),dic.keys())))