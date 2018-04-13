# dict = {"name":"tom","age":18,"content":["abcd",1,2,33,1,("abc","tom","jerry",{"gender":"F","class":23,True:123})]}
# print(dict)
# v = dict["content"][5][3]["gender"]
# print(v)
#
#
# dict2 = {(123,"abc"):123}
# print(dict2)
# dict1 = {1:11,2:22,1:33,3:33,4:44}
# print(dict1)
#
# del dict["content"][5][3][True]
# dict = {"name":"tom","age":18,"content":["abcd",1,2,33,1,("abc","tom","jerry",{"gender":"F","class":23,True:123})]}
# for i,j in dict.items():
#     print(i,j)

# v2 = dict.fromkeys([11,22,33,44],["aa","bb"])
# print(v2)

dict = {"k1":"a","k2":"b","k3":"c",1:"a",2:"b"}
dict.update(k1="aaa",k5="ee")
print(dict)
