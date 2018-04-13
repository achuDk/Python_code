# def test(x):
#     y = 2 * x + 1
#     # return x,y
#     # return x
#     # return y
#     return {y,2,((x,y),1),x}
# print(test(x=1+2**3))
# print(z)
# def test():
#     x = 2
#     y = x * 2 + 1
#     return y
# z = test()
# print(z)

# def res(x,y):
#     res = x ** y
#     return x
# # print(x)
# z = res(2,3)
# # print(x)
# print(z)
#
# def test(x,y,z):
#     print(x)
#     print(y)
#     print(z)
# test(1,2,[1,2])
# test(y=1,x=2,z=3)
# test(1,2,z=2)

# def test(a,b='123',*args):
#     print(a)
#     print(b)
#     print(args)
#     print(args[-1])
# test(1)
# test(2,312)
# test(*[1,2,3])
# print(test({2:'b'},*[1,2,3,*['a','b'],5,7,8,9,{1:'a'}]))

# def test(x,*args,**kwargs):
#     print(x)
#     print(args,args[-1])
#     print(kwargs)
#     print(kwargs.get('a'))
# # test('c',123,'wwer',123,c=1,a=3,b=5)
# test(1,*[1,2,3,'w',35,3345,12],**{'name':'alex','age':12})
# test(1,**{'y':1,'z':2})

# i = 1
# j = 9
# while i < 10:
#     while j > 0 :
#         print(' ' * j,'*' * i)
#         i += 2
#         j -= 1

# def test(x,y,z):
#     res = x ** y + z
#     return 'res:',res
# i = test(1,2,3)
# print(i)
# def test(x,y,z):
#     res = x ** y + z
#     return 'res:',res
# i = test(y=1,x=1,z=3)
# # print(i)
# def test(y,z,x=1):
#     res = x + y + z
#     return x,y,z,res
# print(test(2,3))
#
# def test(y,z,x=1):
#     res = x + y + z
#     return x,y,z,res
# print(test(2,3,x=10))

