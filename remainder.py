T = int(input(""))
res = []

for i in range(T):
    A, B  = input("").split() 
    result = 0
    result += int(A) % int(B)
    res.append(result)

for i in res:
    print(i)
