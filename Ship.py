T = int(input())
res = []

ship = {"B":"BattleShip", "C":"Cruiser", "D":"Destroyer", "F":"Frigate"}

for i in range(T):
    x = input("")
    res.append(ship[x.upper()])

for i in res:
    print(i)