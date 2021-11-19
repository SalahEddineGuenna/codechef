from types import resolve_bases


def coprime(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


def main():
    T = int(input())
    res = []

    for i in range(T):
        x, y = input().split()
        n = int(x)
        m = int(y)
        res.append(str(coprime(n, m)) + " " + str(compute_lcm(n, m)))

    for i in res:
        print(i)

        
main()