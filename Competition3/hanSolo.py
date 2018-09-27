def slope(x1, y1, x2, y2):
    denom = (x2-x1)
    return (y2-y1)/denom if denom != 0 else "indefinido"
def minShotsRequired(x0, x1, n, stormtroopers):
    slopes = {}
    different = 0
    for i in range(n):
        m = slope(x0, y0, stormtroopers[i][0], stormtroopers[i][1])
        if not slopes.get(m):
            slopes[m] = True
            different +=1
    return different 
n, x0, y0 = [int(x) for x in input().split()]
stormtroopers = []
for i in range(n):
    tmp = [int(x) for x in input().split()]
    stormtroopers.append((tmp[0], tmp[1]))
print(minShotsRequired(x0,y0,n,stormtroopers))