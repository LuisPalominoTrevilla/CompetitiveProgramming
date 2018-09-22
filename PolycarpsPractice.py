def getMaxProfit(n, k, problems):
    if k == 1:
        return str(max(problems)) + "\n" + str(n)
    max_indices = {}
    max_profit = 0
    for i in range(k):
        curr_max = 0
        while(max_indices.get(curr_max) is not None):
            curr_max += 1
        for j in range(curr_max,n):
            if max_indices.get(j) is None and problems[j] > problems[curr_max]:
                curr_max = j
        max_profit+=problems[curr_max]
        max_indices[curr_max] = True
    max_indices = list(max_indices.keys())
    max_indices.sort()
    problems_size = str(max_indices[1]) + " "
    for i in range(1, len(max_indices)-1):
        problems_size += str(max_indices[i+1]-max_indices[i]) + " "
    problems_size += str(n-max_indices[len(max_indices)-1])
    return str(max_profit) + "\n" + problems_size
n, k = input().split()
problems = [int(x) for x in input().split()]
print(getMaxProfit(int(n), int(k), problems))