# 函数嵌套
# def f_father():
#     print('a')
#     def f_son():
#         print('b')
#         def f_grandson():
#             print('c')
#         f_grandson()
#     f_son()
# f_father()



# 闭包
# a = 'a'
# b = 'b'
# def f_father(a):
#     print('a:',a)
#     def f_son():
#         print('b:',b)
#         def f_grandson():
#             b = 'bbb'
#             print('b:',b)
#             global c
#             c = 'ccc'
#             print('c:',c)
#         f_grandson()
#     f_son()
# f_father('aaa')
# print('c:',c)

# name = 'aaa'
# def test(func):
#     name = 'bbb'
#     func()
# def foo():
#     print(name)
# test(foo)

# import time
# def foo(a):
#     print('函数foo开始执行...')
#     time.sleep(1.5)
#     print('函数foo执行完毕。')
#     return a
# def time_counter(func):
#     def wrapper(a):
#         start = time.time()
#         func(a)
#         stop = time.time()
#         print('time_counter函数统计结果: %s s' %(stop - start))
#         return a
#     return wrapper
# foo = time_counter(foo)
# res = foo('aaa')
# print('a:',res)


#语法糖
# import time
# def time_counter(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         res = func(*args)
#         stop = time.time()
#         print('time_counter函数统计结果: %s s' %(stop - start))
#         return res
#     return wrapper
#
# @time_counter
# def foo(a):
#     print('函数foo开始执行...')
#     time.sleep(1.5)
#     print('函数foo执行完毕。')
#     return a
# res = foo('aaa')
# print('a:',res)
# foo('aaa')
# @time_counter
# def bar():
#     print('函数bar开始执行...')
#     time.sleep(1)
#     print('函数bar执行完毕。')
# bar()


# import time
# def time(time_zone):
#     def time_counter(func):
#         def wrapper(*args,**kwargs):
#             if time_zone == '东8区':
#                 print(time_zone)
#                 res = func(*args,**kwargs)
#                 return res
#             elif time_zone == '西2区':
#                 print(time_zone)
#                 res = func(*args, **kwargs)
#                 return res
#         return wrapper
#     return time_counter
#
# @time('东8区')
# def foo():
#     print('函数foo')
# foo()
# @time('西2区')
# def bar():
#     print('函数bar')
# bar()

import time
def times(time_zone):
    def time_counter(func):
        def wrapper(*args,**kwargs):
            print(time_zone)
            start = time.time()
            res = func(*args)
            stop = time.time()
            print('time_counter函数统计结果: %s s' %(stop - start))
            return res
        return wrapper
    return time_counter

@times('东八区')
def foo(a):
    print('函数foo开始执行...')
    time.sleep(1.5)
    print('函数foo执行完毕。')
    return a
res = foo('aaa')
print('a:',res)
@times('西二区')
def bar():
    print('函数bar开始执行...')
    time.sleep(1)
    print('函数bar执行完毕。')
bar()