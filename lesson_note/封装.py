class Humanbeings:
    star = 'earth'
    _time = 'now'
    __test = 'test123'
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def get_test(self):
        print(self.__test)

h1 = Humanbeings('tom','white')
print(h1.star)
print(h1._time)

'''
外部无法直接访问到，因为以“ __ ”开头的变量被重命名了
print(h1.__test)  ---> 会报错 
'''
print(h1._Humanbeings__test)

"内部可以直接访问到"
h1.get_test()