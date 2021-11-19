def check(x, y, z):
    if(x + y + z == 180):
        return "YES"

    return "NO"


T = int(input(""))
res = []

for i in range(T):
    x, y, z = input("").split()
    l = int(x)
    m = int(y)
    n = int(z)
    res.append(check(l, m, n))

for i in res:
    print(i)