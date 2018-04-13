
def dog(name,type):
    def init(name,type):
        dog = {
            'name':name,
            'type':type,
            'bark':bark,
            'eat':eat,
        }
        return dog
    def bark(obj):
        print('%s 在叫' %obj['name'])
    def eat(obj=dog):
        print('%s 喜欢吃骨头' %obj['type'])
    return init(name,type)
d1 = dog('喵喵','藏獒')
# print(d1)
d1['bark'](d1)