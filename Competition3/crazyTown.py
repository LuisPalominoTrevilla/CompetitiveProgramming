def getMinSteps(x1, y1, x2, y2, n, lines):
    min_steps = 0
    for i in range(n):
        a = lines[i][0]
        b = lines[i][1]
        c = lines[i][2]
        if (a*x1+b*y1+c)*(a*x2+b*y2+c) < 0:
            min_steps+=1
    return min_steps
x1, y1 = [int(x) for x in input().split()]
x2, y2 = [int(x) for x in input().split()]
n = int(input())
lines = []
for i in range(n):
    line = [int(x) for x in input().split()]
    lines.append((line[0], line[1], line[2]))
print(getMinSteps(x1, y1, x2, y2, n, lines))