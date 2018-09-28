def findMin(n, m):
    sum = 0
    if n >= m:
        return n-m
    while(n < m):
        if m%2 != 0:
            m+=1
        else:
            m//=2
        sum+=1
    return sum+(n-m)
n, m = [int(x) for x in input().split()]
print(findMin(n, m))