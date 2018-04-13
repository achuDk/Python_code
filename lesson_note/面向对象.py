# def dog(name,breed,hobby):
#     def crow(x):
#         print('%s 在叫' %name)
#         # print('狗在叫')
#     def eat(x):
#         print('%s 在吃东西' %breed)
#         # print('狗在吃东西')
#     def init(name,breed,hobby):
#         attr={
#             'name':name,
#             'breed':breed,
#             'hobby':hobby,
#             'crow':crow,
#             'eat':eat,
#         }
#         return attr
#     return init(name,breed,hobby)
# #创建第一个对象并调用方法
# d1 = dog('hachi','qiutian','bones')
# d1['crow'](d1)
# #创建第二个对象并调用方法
# d2 = dog('puppy','jingba','meat')
# d2['eat'](d2)

#面向对象
# abc = '222'
class animal:
    abc = '111'
    def __init__(self,name,breed,attr):
        self.name = name
        self.breed = breed
        self.attr = attr
    def eat(self):
        print('%s在吃东西' %self.name)
    def drink(self):
        print('%s喝水' %self.breed)
    def hobby(self):
        print('%s 喜欢 %s' %(self.name,self.attr))
# people = animal
people = animal('tom','human','play')
print(people.__dict__)
print(people.name)
print(people.abc)
people.eat()
people.drink()
people.hobby()

pixiu = animal('貔貅','神兽','只吃不拉')
print(pixiu.name,pixiu.breed,pixiu.attr)
pixiu.hobby()