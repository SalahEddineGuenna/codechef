def withdraw(x, y):
    if(x % 5  == 0 & x + 0.50 <= y):
        y = y - (x + 0.50)
        return y
    return y


x, y = input("").split()
n = int(x)
m = float(y)
n = withdraw(n, m)
print(n)