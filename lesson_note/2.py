i=0
sum=0
while i < 99:
    if i%2 == 1:
        sum=sum+i
    else:
        sum=sum-i
    i=i+1
    print(i,sum)
