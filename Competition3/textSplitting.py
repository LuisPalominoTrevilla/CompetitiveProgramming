def getSplits(n, p, q, s):
    least = min(p, q)
    greatest = max(p, q)
    if least > len(s):
        print(-1)
        return
    if len(s)%greatest == 0:
        index = greatest
    else:
        index = least
    prev = 0
    words = []
    while True:
        if index > len(s):
            print(-1)
            return
        words.append(s[prev:index])
        prev = index
        if index == len(s):
            break
        if (len(s)-index)%greatest == 0:
            index += greatest
            continue
        elif (len(s)-index)%least == 0:
            index += least
            continue
        else:
            index += least      
    print(len(words))
    for word in words:
        print(word)
n, p, q = [int(x) for x in input().split()]
s = input()
getSplits(n, p, q, s)