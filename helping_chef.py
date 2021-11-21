def main():
    res = []
    T = int(input(""))
    for i in range(T):
        x = int(input(""))
        res.append("Thanks for helping the chef" if (x < 10) else -1)
    for i in res:
        print(i)

main()