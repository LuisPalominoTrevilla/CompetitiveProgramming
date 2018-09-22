def songsCompression(songs, n, capacity, sum):
    songs.sort(reverse=True)
    compressed=0
    if sum <= capacity: return 0
    for song in songs:
        if sum - song > capacity:
            sum-= song
            compressed+=1
        else:
            compressed+=1
            return compressed
    return -1
n, capacity = input().split()
songs = []
sum = 0
for i in range(int(n)):
    line = input().split()
    sum += int(line[0])
    songs.append(int(line[0])-int(line[1]))
print(songsCompression(songs, int(n), int(capacity), sum))