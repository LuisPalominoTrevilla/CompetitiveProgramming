def getBits(n, a, b):
    if "0" not in a or "1" not in a or "0" not in b:
        return 0
    visited0, visited1 = 0, 0
    swaps = 0
    num0a = a.count("0")
    num1a = a.count("1")
    for i in range(n):
        if b[i] == '0':
            if a[i] == '0':
                visited0+=1
                swaps += num1a-visited1
            else:
                visited1+=1
                swaps += num0a-visited0
    return swaps

n = int(input())
a = input()
b = input()

print(getBits(n, a, b))