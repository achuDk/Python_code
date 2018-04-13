class H2o:
    def __init__(self,name,temperature):
        self.name = name
        self.temperature = temperature
    def convert(self):
        if True:
            if self.temperature < 0:
                print('%s 要变成冰了' %self.name)
            elif self.temperature >= 0 and self.temperature < 100:
                print('%s 变成了液态水' %self.name)
            elif self.temperature >= 100:
                print('%s 呈现气态' %self.name)
        else:
            print('对象定义有误，请重新检查')

class Water(H2o):
    pass
    # def __init__(self,temperature):
    #     self.temperature = temperature
class Ice(H2o):
    # def __init__(self,temperature):
    #     self.temperature = temperature
    pass
class Steam(H2o):
    # def __init__(self,temperature):
    #     self.temperature = temperature
    pass
w1 = Water('水',15)
i1 = Ice('冰',-20)
s1 = Steam('蒸汽',120)
print(w1.__dict__)

# w1.convert()
# i1.convert()
# s1.convert()
def func(obj):
    obj.convert()
func(w1)
func(i1)
func(s1)