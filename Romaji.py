def isBerlanese(word):
    vowels = "aeiou"
    n = len(word)
    if word[n-1] != 'n' and word[n-1] not in vowels:
        return 'NO'
    for i in range(n-1):
        if word[i] not in vowels and word[i] != 'n' and word[i+1] not in vowels:
            return 'NO'
    return 'YES'
print(isBerlanese(input()))