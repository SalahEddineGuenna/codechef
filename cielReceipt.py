def toList(x):
    res = []
    count = 0
    temp = '{0:012b}'.format(x)
    strtemp = str(temp)
    for i in strtemp:
        res.append(int(i))

    for i in res:
        if(i == 1):
            count += 1

    return count


T = int(input())
res = []
for i in range(T):
    x = int(input())
    res.append(toList(x))

for i in res:
    print(i)
