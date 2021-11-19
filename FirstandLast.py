T = int(input(""))
res = []

for i in range(T):
    x = input("")
    M = [int(m) for m in x]
    result = 0
    result = M[0] + M[-1]
    res.append(result)

for i in res:
    print(i)