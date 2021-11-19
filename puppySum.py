def Sum(N):
    sum = 0
    for i in range(1, N + 1):
        sum += i

    return sum

def puppysum(D, N):
    sum = N
    for i in range(D):
        sum = Sum(sum)

    return sum


def main():
    T = int(input())
    res = []
    for i in range(T):
        x, y = input().split()
        D = int(x)
        N = int(y)
        res.append(puppysum(D, N))

    for i in res:
        print(i)


main()
