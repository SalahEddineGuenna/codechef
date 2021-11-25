def main():
    T = int(input())
    res = []
    for i in range(T):
        n, k = map(int,input().split())
        mx = 0
        for j in range(1, k+1):
            r = n % j
            if(r > mx):
                mx = r
        res.append(mx)
    for i in res:
        print(i)

main()
