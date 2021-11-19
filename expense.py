def compute(quantity, price):
    sum = price * quantity
    if (quantity > 1000):
        sum = sum - ((10 * sum)/ 100)
    return sum



def main():
    T = int(input())
    res = []
    for i in range(T):
        x, y = input().split()
        n = int(x)
        m = float(y)
        res.append(compute(n, m))

    for i in res:
        print(i)

main()
        