'''
回调函数的作用是：让回调函数内的内容可以在主线程内进行
'''
from multiprocessing import Pool
import os,time

def foo(i):
    time.sleep(1)
    print('process_%s' %i,'\t',os.getpid(),'\t',time.strftime('%X'))
    return '>>hello!<<'

def bar(arg):
    print('bar:','\t\t',os.getpid(),'\t',arg)

if __name__ == '__main__':
    for i in range(20):
        p = Pool(5)
        # p.apply(func=foo,args=(i,))                     #同步模式：串行
        p.apply_async(func=foo,args=(i,),callback=bar)    #异步模式：并行（并发）

    p.close()           #close()必须在join()之前，否则报错
    p.join()
    print('ending...')
