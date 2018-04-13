"""
在子类中调用父类的属性时，有三种方法，三种方法执行结果是一模一样的，在子类中执行：
1. 使用 [ 父class名.属性名             ] 来调用，如：Vehicle.__init__(self,name)
2. 使用 [ super().属性名              ] 来调用，如：super().__init__(name)
3. 使用 [ super(__class__,self).属性名] 来调用，如：super(__class__,self).__init__(name)


注意：二者的区别：
1. 使用super()函数无需传递 self 参数
2. 如果父类名字更改了，所有调用了的子类中的名字都要更改，所以更建议使用super()函数的方法

【更建议使用第二种 super() 函数的方法】

"""

class Vehicle:
    def __init__(self,name,speed,power):
        self.name = name
        self.speed = speed
        self.power = power

    def startup(self):
        print('%s 准备启动' %self.name)

class Bicycle(Vehicle):
    def __init__(self,name,speed,power,type):
        Vehicle.__init__(self,name,speed,power)
        #或者使用 super() 函数，注意，使用super()函数无需传self值
        super().__init__(name,speed,power)
        #或者：
        super(__class__,self).__init__(name,speed,power)
        self.type = type

    def startup(self,speed):
        Vehicle.startup(self)
        #或者使用 super() 函数，super()函数无需传self值
        super().startup()
        #或者使用：
        super(__class__,self).startup()
        print('以 %sm/s 的速度启动' %speed)

b1 = Bicycle('摩拜',5,'labor','shared')
print(b1.__dict__)
b1.startup(5)
Bicycle.startup(b1,5)