def main():
    T = int(input(""))
    winner = diff = lead = n = m = 0
    for i in range(T):
        x, y = input("").split()
        n += int(x)
        m += int(y)
        if(n > m):
            diff = n - m
            if(diff > lead):
                winner = 1;
                lead = diff
        else:
            diff = m - n
            if(diff > lead):
                winner = 2
                lead = diff

    print(winner, lead)

main()
