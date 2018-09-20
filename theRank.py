def getRank(grades):
    thomas_rank = 1
    thomas_grade = grades[0]
    for grade in grades:
        if thomas_grade < grade:
            thomas_rank+=1
    return thomas_rank

n = int(input())
grades = []
for i in range(n):
    grades.append(sum([int(x) for x in input().split()]))
print(getRank(grades))