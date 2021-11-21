T = int(input(""))
res = []

for i in range(T):
    x = input("")
    M = [int(m) for m in x]
    res.append(M[0] + M[-1])

for i in res:
    print(i)