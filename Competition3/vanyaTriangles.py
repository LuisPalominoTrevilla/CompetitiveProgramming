def slope(x1, y1, x2, y2):
    denom = (x2-x1)
    return (y2-y1)/denom if denom != 0 else "Indefinido"
def isTriangle(point1,point2,point3):
    m1 = slope(point1[0],point1[1],point2[0],point2[1])
    m2 = slope(point1[0],point1[1],point3[0],point3[1])
    return True if m1 != m2 else False
def getPossibleTriangles(n,points):
    res = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if isTriangle(points[i], points[j], points[k]):
                    res += 1
    return res
n = int(input())
points = []
for i in range(n):
    point = [int(x) for x in input().split()]
    points.append((point[0], point[1]))
print(getPossibleTriangles(n, points))