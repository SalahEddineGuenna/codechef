def reverse(number):
    revs_number = 0
    while (number > 0):  
        remainder = number % 10  
        revs_number = (revs_number * 10) + remainder  
        number = number // 10

    return revs_number

T = int(input())
res = []

for i in range(T):
    x = int(input())
    if(x == reverse(x)):
        res.append("wins")
    else:
        res.append("loses")

for i in res:
    print(i)