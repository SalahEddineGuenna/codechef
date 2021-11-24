def main():
    cmpt = 0
    T, k = input().split()
    T = int(T)
    k = int(k)
    for i in range(T):
        x = int(input())
        if(x % k == 0):
            cmpt += 1
    print(cmpt)

main()
