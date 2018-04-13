import time
# def producer(num):
#     for i in range(1,num):
#         print('生产第%s屉包子' %i)
#         yield i
# def consumer(num):
#     p = producer(num)
#     for a in p:
#         time.sleep(0.5)
#         print('吃掉第%s屉包子' %a)
#         time.sleep(1)
# c = consumer(5)



# def consumer(name):
#     while True:
#         baozi = yield
#         print('%s吃掉了%s' %(name,baozi))
# def producer(name,num):
#     c = consumer(name)
#     next(c)
#     for i in range(1,num):
#         print('生产了第%s屉包子' %i)
#         c.send('第%s屉包子' %i)
# p =producer('obama',5)


# def generator(num,name):
#     print('开始')
#     for i in range(num):
#         fruit = yield name
#         print('【%s】喜欢吃【%s】' %(name,fruit))
# g = generator(3,'tom')
# g.send(None)
# g.send('orange')
# g.send('apple')


# def producer(num,name):
#     print('%s开始吃苹果' %name)
#     while True:
#         fruit = yield
#         print('【%s】吃掉了一个【%s】' %(name,fruit))
# def consumer(num,name):
#     g = producer(num,name)
#     next(g)
#     for i in range(num):
#         g.send('apple')
# consumer(2,'jerry')
# consumer(3,'tom')

