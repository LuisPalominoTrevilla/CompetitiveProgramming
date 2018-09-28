def getMinCost(w, guns):
    cost = 0
    for gun in guns:
        cost += gun[0]*w
        w *= gun[1]
    return cost
n, w = [int(x) for x in input().split()]
guns = []
for i in range(n):
    line = input().split()
    guns.append((float(line[0]), float(line[1])))
guns.sort(key=lambda tup: (tup[0]*tup[1]))
print(getMinCost(w, guns))