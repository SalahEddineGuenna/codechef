T = int(input(""))
res = []

for i in range(T):
    tmp = []
    A, B, C  = input("").split() 
    tmp.extend([int(A), int(B), int(C)])
    tmp.sort()
    res.append(tmp[1])


for i in res:
    print(i)
