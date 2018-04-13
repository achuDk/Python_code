import time
# def generator():
#     for i in range(4):
#         yield i
#         time.sleep(1)
# g = generator()
# print(g)
# for i in g:
#     print(i)
#     print('第%s次\n' %i)

# list = [i for i in range(10)]
# list1 = (i for i in range(10))
# print(list,'\n',list1)
# print(next(list1))
# print(next(list1))

# def xiadan():
#     for i in range(10):
#         yield 'egg%s' %i
# for i in range(5):
#     x = xiadan()
#     s = next(x)
#     print(s)

# def lay_egg(num):
#     for i in range(num):
#         yield 'egg%s' %i
# laomuji = lay_egg(5)
# print(laomuji)
# print(next(laomuji))
# print(next(laomuji))
# print(next(laomuji))
# egg_list = list(laomuji)
# print(egg_list)
# import this
# print(this)


from functools import reduce

def iter(file):
    with open(file,'r',encoding='utf-8') as f:
        for i in f:
            yield i
s = iter('人口.py')
# print(s)
# print(next(s))
# print(next(s))
m = eval(next(s))['population']
n = eval(next(s))['population']

print(m,n)
# o = next(s)
# print(type(o),o)
# p = eval(o)
# print(type(p),p)
# q = p['population']
# print(type(q),q)
# r = reduce(lambda x,y:x+y,list(q))
# print(r)