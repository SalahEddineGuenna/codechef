def small(numbers):
    min = numbers[0] + numbers[1]
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            temp = numbers[i] + numbers[j]
            if(temp < min):
                min = temp

    return min


def main():
    T = int(input())
    res = []
    for i in range(T):
        N = int(input())
        numbers = [int(i) for i in input().split()][:N]
        res.append(small(numbers))

    for i in res:
        print(i)

main()

