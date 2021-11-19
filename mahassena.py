count1 = 0
count2 = 0

N = int(input(""))
res = [int(i) for i in input("").split()][:N]
for i in res:
    if (i % 2 == 0):
        count1 += 1
    else:
        count2 += 1

if (count1 > count2):
    print("READY FOR BATTLE")
else:
    print("NOT READY")
