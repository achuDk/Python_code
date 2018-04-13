"""
定义楼层范围
确定电梯上行或下行
在确定电梯上下行前要收集乘客按电梯的先后顺序
收集乘客按的电梯楼层数字
"""
#定义总楼层数
floor_max = 15
floor_min = -3
#定义乘客已选的楼层
floors = []
#
floor_run = []

def collector():
    floor = int(input('请输入您想到达的楼层数（-3 ~ 16层）： ').strip())
    if not floor:
        if floor > 0:
            floor = floor -1
        floors.append(floor)
        print('当前列表：%s' %floors)
        #去重
        floor_uniq = list(set(floor))
        print('去重后当前列表：%s' %floors_uniq)

def run():
    #定义电梯上下行
    if floor_cur < floor[0]:
        print('电梯上行...')
        for i in floors:
            if i not in floor_run and i >= floor_cur and i <= floor[0]:
                floors.pop(i)
                floor_run.append(i)


def stop():
    print('当前楼层：%s' %floor_cur)




# 定义电梯当前位置
# floor_cur = 0
