class Foo:
    def __init__(self,n):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n <= 6:
            self.n += 1
            return self.n
        raise StopIteration
# f1 = Foo(0)
# print(f1.__next__())
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
#
# f2 = Foo(5)
# for i in f2:
#     print(i)

class Bar:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= self.stop/2:
            self.start *= 2
            return self.start
        else:
            raise StopIteration("\n\n -_-# \n out of range!!!!! \n -_-#")
b1 = Bar(1,10)
print(b1.__next__())
print(b1.__next__())
print(b1.__next__())
print(b1.__next__())
print(b1.__next__())
