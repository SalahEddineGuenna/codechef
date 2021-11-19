def check(x, y):
    if(x > y):
        return ">"
    elif(x < y):
        return "<"
    else:
        return "="


T = int(input(""))
res = []

for i in range(T):
    x, y = input("").split()
    n = int(x)
    m = int(y)
    res.append(check(n, m))

for i in res:
    print(i)