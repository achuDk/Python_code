# import threading
# import time
#
# def listen():
#     print('listen music\t\t %s' %time.ctime())
#     time.sleep(3)
#     print('listen end\t\t\t %s' %time.ctime())
# def book():
#     print('read\t\t\t\t %s'  %time.ctime())
#     time.sleep(5)
#     print('read ending\t\t\t %s' %time.ctime())
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=listen)
#     t1.start()
#     t2 = threading.Thread(target=book)
#     t2.start()
#
#     # t1.join()
#     # t2.join()
#     print('total ending...\t\t %s' %time.ctime())


# import threading,time
#
# def test1():
#     print('test1')
#     time.sleep(2)
#
# def test2():
#     print('test2')
#     time.sleep(1)
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=test1)
#     t2 = threading.Thread(target=test2)
#     t1.start()
#     t2.start()
#     print('main thread ending')


import threading,time

class Mythread(threading.Thread):
    def __init__(self,num):
        super().__init__()
        # threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print(self.name,'start')
        time.sleep(self.num)
        print(self.name,'stop')

if __name__ == '__main__':
    l = []
    t1 = Mythread(2)
    t2 = Mythread(1)
    l.append(t1)
    l.append(t2)

    t1.setDaemon(True)

    t1.start()
    t2.start()

    # for i in l:
    #     i.join()

    print('main thread ending...')