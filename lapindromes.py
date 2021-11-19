from collections import Counter
def main():
    T = int(input())
    res = []
    for i in range(T):
        s = input()
        s1 = s[:len(s)//2]
        if(len(s) % 2 == 0):
            s2 = s[len(s) // 2:]
        else:
            s2 = s[len(s) // 2 + 1:]
        if(Counter(filter(str.isalnum, s1)) == Counter(filter(str.isalnum, s2))):
            res.append("YES")
        else:
            res.append("NO")

    for i in res:
        print(i)

main()