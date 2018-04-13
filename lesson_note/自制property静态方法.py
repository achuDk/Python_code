"""
原始方法
"""
# class Room:
#     def __init__(self,name,width,length):
#         self.name = name
#         self.width = width
#         self.length = length
#     def area(self):
#         return self.width * self.length
# r1 = Room('厕所',1,1)
# print(r1.area())

"""
使用 @proterty 转换为静态方法
"""
# class Room:
#     def __init__(self,name,width,length):
#         self.name = name
#         self.width = width
#         self.length = length
#     @property
#     def area(self):
#         return self.width * self.length
# r1 = Room('厕所',1,1)
# print(r1.area)
# print(Room.area)

"""
手动实现静态方法：通过装饰器和描述符，装饰器可以是类
"""
class Manualproperty:
    def __init__(self,func):
        print("__init__函数执行======>",func)
        self.func = func
    def __get__(self, instance, owner):
        print(self.func,"__get__函数执行======>",instance,owner)
        if instance != None:
            return self.func(instance)
        else:
            return self
class Room:
    def __init__(self,name,width,length):
        self.name = name
        self.width = width
        self.length = length
    """语法糖此处代表执行了 area=Manualproperty(area) 操作
            此时Manualproperty是一个类，area是这个类的一个实例
            并且，area=Manualproperty(area) 该操作实现了给Room类增加了一个描述符的功能
            所以：Manualproperty 是一个装饰器类，并且是Room类的描述符"""
    @Manualproperty
    def area(self):
        return self.width * self.length
    def test(self):
        return 'test'
    test = Manualproperty(test)         #模拟语法糖的效果

r1 = Room('厕所',1,1)
print(r1.area)     #触发了 Manualproperty 这个类内置函数 __init__ 和 __get__ 的执行
# print(Room.__dict__)
# print(r1.__dict__)

r2 = Room('test',1,1)
print(r2.test)

print(Room.area)