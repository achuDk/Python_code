"""实现对一个文件写入的内容，每行前面加上时间"""
class Filehandle:
    def __init__(self,name,mode='r',encoding='utf-8'):
        self.name = name
        self.file = open(name,mode,encoding=encoding)
        self.mode = mode
        self.encoding = encoding
    def __getattr__(self, item):
        print('执行__getattr__函数 %s:' %item)
        return getattr(self.file,item)

f1 = Filehandle('a.txt','r+')
print(f1.name)
print(f1.__dict__)
f1.write('111111111\n')
f1.seek(0)
print(f1.read())