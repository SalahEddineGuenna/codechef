def maxi(tab):
    max = 0
    for i in tab:
        if max < i:
            max = i

    return tab.index(max)


T = int(input(""))

winner = []
diff = []

for i in range(T):
    x, y = input("").split()
    n = int(x)
    m = int(y)
    if(n > m):
        winner.append(1)
        diff.append(n - m)
    else:
        winner.append(2)
        diff.append(m - n)

index = maxi(diff)
print(winner[index], diff[index])
