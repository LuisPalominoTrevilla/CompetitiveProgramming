def getPassword(s):
    possible_pass = ""
    j = len(s)-1
    final_pass = ""
    for i in range(j-1):
        possible_pass = s[0:i+1]
        if possible_pass == s[j-i:j+1] and possible_pass in s[1:j]:
            final_pass = possible_pass
    return 'Just a legend' if final_pass == "" else final_pass
s = 'a'*10**6
print(getPassword(s))