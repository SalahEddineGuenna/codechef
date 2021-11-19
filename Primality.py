def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


T = int(input())
res = []

for i in range(T):
    x = int(input())
    if(is_prime(x)):
        res.append("yes")
    else:
        res.append("no")

for i in res:
    print(i)