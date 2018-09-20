def pointsInSegments(coordinates, m):
    coordinates.sort(key=lambda tup: tup[0])
    curr_segment = 0
    not_belonging = ""
    for curr_num in range(1, m+1):
        while curr_segment < len(coordinates):
            if coordinates[curr_segment][0] > curr_num:
                not_belonging += str(curr_num) + " "
                break
            if (coordinates[curr_segment][0] <= curr_num and coordinates[curr_segment][1] >= curr_num):
                break
            curr_segment+=1
        if curr_segment >= len(coordinates):
            not_belonging += str(curr_num) + " "
    if not_belonging == "":
        return "0\n"
    else:
        return str(len(not_belonging.split()))+"\n"+not_belonging

data = input().split()
n = int(data[0])
m = int(data[1])
segments = []
for i in range(n):
    segment = input().split()
    segments.append((int(segment[0]), int(segment[1])))

print(pointsInSegments(segments, m))