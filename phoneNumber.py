def phoneNumber(n):
    if n == 1:
        return "1 "
    permutation = ""
    for i in range(n//2+1,n+1):
        permutation+= str(i) + " "
    permutation+=fillSecondSpace(n//2, n)
    return permutation
def fillSecondSpace(n, real):
    if n == 1:
        return "1 "
    res=""
    for i in range(1, n+1):
        res+=str(i)+" "
    return res
print(phoneNumber(int(input())))