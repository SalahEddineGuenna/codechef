import math

T = int(input(""))
res = []

for i in range(T):
    x = int(input(""))
    res.append(int(math.sqrt(x)))

for i in res:
    print(i)