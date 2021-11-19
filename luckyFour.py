T = int(input(""))
res =[]

for i in range(T):
    x = input("")
    M = [int(m) for m in x]
    cmpt = 0
    for i in M:
        if i == 4:
            cmpt += 1
    res.append(cmpt)

for i in res:
    print(i)
