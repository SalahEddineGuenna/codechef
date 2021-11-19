T = int(input(""))
res = []
result = 0

for i in range(T):
    x = input("")
    M = [int(m) for m in x]
    result = 0
    for i in M:
        result += i
    res.append(result)

for i in res:
    print(i)



