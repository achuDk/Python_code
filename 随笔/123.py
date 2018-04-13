# l = [1,2,3,4,87,23,1,78,9,]
# print(l)
# print(l[6])
#
# l = list(set(l))
# print(l)
# print(l[6])
#
# l = list(set(l))
# print(l)
# print(l[6])



l = [0,1,2,3,4,5,6]
for i in l:
    l.pop(l.index(i))
if len(l) == 0:
    print('yes')
else:
    print('fool')