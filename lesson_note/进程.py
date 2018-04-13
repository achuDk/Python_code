"""方法1"""
# import multiprocessing,time
#
# def action1():
#     print('action1 start...\t',time.ctime())
#     time.sleep(3)
#
# def action2():
#     print('action2 start...\t',time.ctime())
#     time.sleep(2)
#
# if __name__ == '__main__':
#     l = []
#     t1 = multiprocessing.Process(target=action1)
#     t2 = multiprocessing.Process(target=action2)
#     l.append(t1)
#     l.append(t2)
#     t1.start()
#     t2.start()
#     for i in l:
#         i.join()
#     print('ending...\t\t\t',time.ctime())


"""方法2"""

import multiprocessing,time

class Myprocess(multiprocessing.Process):
    def __init__(self,num):
        super().__init__()
        # multiprocessing.Process.__init__(self)
        self.num = num
    def run(self):
        print(self.name,'start...\t',time.ctime())
        time.sleep(self.num)

if __name__ == '__main__':
    p1 = Myprocess(2)
    p2 = Myprocess(3)

    p1.daemon = True

    p1.start()
    p2.start()

    # p1.join()
    # p2.join()

    print('main process ending...\t',time.ctime())