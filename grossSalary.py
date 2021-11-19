def gross(salary):
    grs = salary
    if(salary < 1500):
        HRA = (10 * salary) / 100
        DA = (90 * salary) / 100
        grs += HRA + DA 
    else:
        HRA = 500
        DA = (98 * salary) / 100
        grs += HRA + DA
    return grs

def main():
    T = int(input())
    res = []
    for i in range(T):
        x = float(input())
        res.append(gross(x))

    for i in res:
        print(i)

main()
