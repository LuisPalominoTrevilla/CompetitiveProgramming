import math
import sys

def pairOfToys(toys, k):
    if k > toys*2:
        return 0
    numWays = math.ceil((toys-abs(toys-k))/2)
    return numWays if (k>toys) else (numWays-1)

inputs = input().split(" ")
toys = int(inputs[0])
k = int(inputs[1])
print(pairOfToys(toys, k))