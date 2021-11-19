def check(n):
    if(n < 10):
        return "Thanks for helping the Chef!"
    else:
       return -1


res = []
T = int(input(""))

for i in range(T):
    x = int(input(""))
    res.append(check(x))

for i in res:
    print(i)