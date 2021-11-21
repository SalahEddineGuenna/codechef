def main():
    T = int(input())
    res = []
    for i in range(T):
        N = int(input())
        #string = [x for x in input()][:N]
        s = input()[:N]
        res.append("INDIAN" if ("I" in s) else "NOT INDIAN" if ("Y" in s) else "NOT SURE")
    for i in res:
        print(i)

main()