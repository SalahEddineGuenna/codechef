def conditions(cond1, cond2, cond3):
    result = 0
    if(cond1 == True & cond2 == True & cond3 == True):
        res = 10
        return res
    if(cond1 == True & cond2 == True):
        res = 9
        return res
    if(cond2 == True & cond3 == True):
        res = 8
        return res
    if(cond1 == True & cond3 == True):
        res = 7
        return res
    if(cond1 == True or cond2 == True or cond3 == True):
        res = 6
        return res
    else:
        res = 5
        return res


def steel(x, y, z):
    cond1 = False
    cond2 = False
    cond3 = False
    if(x > 50):
        cond1 = True
    if(y < 0.7):
        cond2 = True
    if(z > 5600):
        cond3 = True
    return conditions(cond1, cond2, cond3)

def main():
    T = int(input())
    res = []
    for i in range(T):
        x, y, z = input().split()
        n = int(x)
        m = float(y)
        l = int(z)
        res.append(steel(n, m, l))

    for i in res:
        print(i)

main()
