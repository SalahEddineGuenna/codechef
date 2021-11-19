def fact(num):
    factorial = 1
    if num == 0:
        return num
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        return factorial





T = int(input(""))
res = []

for i in range(T):
    x = int(input(""))
    res.append(fact(x))

for i in res:
    print(i)