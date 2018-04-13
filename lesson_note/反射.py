#hasattr(),getattr(),setattr(),delattr()
class Vehicle:
    def __init__(self,name,type):
        self.name= name
        self.type = type

    def start(self):
        print('%s 准备启动了' %self.name)


class Bicycle(Vehicle):
    pass

b1 = Bicycle('自行车','非机动车')
print(hasattr(b1,'name'))
print(hasattr(b1,'start'))

s = getattr(b1,'name')
func = getattr(b1,'start','没有这个属性')
print('------------',s,func)
func()
# print(b1.name)
# setattr(b1,'name','摩拜')
# print(b1.name)
# setattr(b1,'abc',123)
# setattr(b1,'123','abc')
# print(b1.__dict__)
#
# del b1.abc
# delattr(b1,'123')
# print(b1.__dict__)