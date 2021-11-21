def main():
    n = int(input())
    res = []
    for i in range(n):
        name = input()
        mark = float(input())
        res.append([name, mark])
    print(res)

main()