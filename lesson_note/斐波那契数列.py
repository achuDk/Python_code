import time
t1 = time.time()
# print(t1,type(t1))
class Fibo:
    a = 0
    b = 1
    i = 0
    def __init__(self,n):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < self.n:
            self.a,self.b = self.b,self.a+self.b
            self.i += 1
            return "第%s次运算：" %self.i,self.b-self.a
        else:
            raise StopIteration
# f1 = Fibo(3)
# print(f1.__next__())
# print(f1.__next__())
# print(next(f1))
# print(next(f1))


f2 = Fibo(100)
for i in f2:
    print(i)
t2 = time.time()
# print(t2,type(t2))
print('运算【%s次】用时：【%s秒】' %(f2.n,(t2-t1)))

# t3 = time.time()
# a = 0
# b = 1
# for i in range(100):
#     print(a+b)
#     a,b = b,a+b
#
# t4 = time.time()
# print('运算用时：【%s秒】' %(t4-t3))