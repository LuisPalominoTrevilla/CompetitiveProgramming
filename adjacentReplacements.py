def mishka(array):
    output = ""
    for num in array:
        if (num%2==0):
            output += str(num-1) + " "
        else: output += str(num) + " "
    return output
n = int(input())
array = [int(x) for x in input().split()]
print(mishka(array))