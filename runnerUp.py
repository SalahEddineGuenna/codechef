def main():
    n = int(input())
    arr = [int(i) for i in input().split()][:n]
    arr.sort()
    arr = list(dict.fromkeys(arr))
    print(arr[-2])

main()