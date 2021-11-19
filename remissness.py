def remis(x, y):
    res = []
    res.append(min(x, y))
    res.append(x + y)
    return res

T = int(input(""))
res = []
for i in range(T):
    x, y = input("").split()
    n = int(x)
    m = int(y)
    res.append(remis(n, m))
    
for i in range(len(res)):
    print(res[i][j])
