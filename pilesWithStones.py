def pileWithStones(x, y, n):
    return 'YES' if y<=x else 'NO'
n = int(input())
x = sum(int(x) for x in input().split())
y = sum(int(y) for y in input().split())
print(pileWithStones(x, y, n))