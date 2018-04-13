# list = ["alex","seven","eric"]
# list.append(123)
# print(list)
# test = list.count("aBC")
# print(test)
# list = ["abc","def","abc","ghi"]
# list.clear()
# print(list)
# list.append()
# print(list)

# list = ["alex","seven","eric"]
# list1 = list.copy()
# print(list1)
# v = list.index("eric")
# print(v)

# list = ["alex","seven","eric"]
# list.insert(1,"abc")
# print(list)

# list = ["alex","seven","eric"]
# pop = list.pop()
# print(list,"\n",pop)

# list = ["abc","alex","seven","eric"]
# del list[0]
# print(list)
# del list[0:1]
# print(list)

# list = ["abc","alex","abc","seven","abc","eric"]
# list.remove("abc")
# print(list)
# list.remove("abc")
# print(list)

# list = ["abc","alex","abc","seven","abc","eric"]
# id(list)
# list.reverse()
# print(list)
# id(list
#

# list = ["abc","alex","abc","seven","abc","eric"]
# list.sort()
# print(list)
# list = [110,22,0,55,33,120,44]
# list.sort()
# print(list)

# list = ["abc","alex","abc","seven","abc","eric"]
# list.extend("不得了")
# print(list)
# list = ["abc","alex","seven","eric"]
# list.extend([11,22])
# print(list)
# list.extend(("abc",45))
# print(list)
# list = ["abc","alex","seven","eric"]
# list.extend({"name":"alex","age":12})
# print(list)
# list = ["abc","alex","seven","eric"]
# list.extend(["xyz",["opq",123],{"vuw":789}])
# print(list)
# v = "alex" in list
# print(v)

# 取出123
# list = ['abc', 'alex', 'seven', 'eric', 'xyz', ['opq', 123], {'vuw': 789}]
# v = list[5][1]
# print(v)
# # 取出789
# list = ['abc', 'alex', 'seven', 'eric', 'xyz', ['opq', 123], {'vuw': 789}]
# v = list[6].values()
# print(v)


li = ["name", 123]
v = tuple(li)
print(v)
tpl = ("name", 123, ["alex", "eric", ("seven", 789), {"name": "tom", "age": 18}])
print(tpl)
x = str(123)
print(type(x))
