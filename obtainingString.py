def obtainSwaps(a, b, n):
    reordered = {}
    i, j = 0, 0
    num_reordered = 0
    swaps = 0
    swap_pos = ""
    while(j < n):
        if b[j] == a[i]:
            i+=1
            while (reordered.get(i) is not None):
                i+=1
            j+=1
            continue
        search_pos = i
        stack = []
        cont = 0
        while(a[search_pos] != b[j]):
            stack.append(j+1+cont)
            cont+=1
            swaps+=1
            search_pos+=1
            while(reordered.get(search_pos) is not None):
                search_pos+=1
            if search_pos == n:
                return -1
        while(len(stack) > 0):
            swap_pos += str(stack.pop()) + " "
        reordered[search_pos] = True
        num_reordered+=1
        j+=1
    return str(swaps)+"\n"+swap_pos
n = int(input())
a = input()
b = input()
print(obtainSwaps(a,b,n))