def withdraw(x, y):
    if(x % 5  == 0 & x <= y):
        y = y - (x + 0.50)
        return y
    return y


x, y = input("").split()
n = int(x)
m = float(y)
if(n <= m):
    n = withdraw(n, m)
print(m)