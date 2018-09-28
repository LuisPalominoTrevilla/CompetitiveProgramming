class Nodo:
    def __init__(self, hasCat, value):
        self.hasCat = hasCat
        self.value = value
        self.neighbors = []
    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)
n, m = [int(x) for x in input().split()]
cats = [int(x) for x in input().split()]
vertices = [None] * (n+1)
for i in range(n-1):
    node1, node2 = [int(x) for x in input().split()]
    if not vertices[node1]:
        vertices[node1] = Nodo(cats[node1-1], node1)
    if not vertices[node2]:
        vertices[node2] = Nodo(cats[node2-1], node2)
    vertices[node1].addNeighbor(vertices[node2])
    vertices[node2].addNeighbor(vertices[node1])
root = vertices[1]
def findNumPaths(root, m, vertices):
    visited = {}
    work = []
    consecutive_cats = []
    possible_paths = 0
    work.append(root)
    while len(work) > 0:
        current = work.pop()
        visited[current.value] = True
        if current is root:
            consec_cats = current.hasCat
        else:
            previous_cats = consecutive_cats.pop()
            if current.hasCat == 0:
                consec_cats = 0
            else:
                consec_cats = current.hasCat+previous_cats
        if consec_cats <= m:
            for neighbor in current.neighbors:
                if not visited.get(neighbor.value):
                    work.append(neighbor)
                    consecutive_cats.append(consec_cats)
            if len(current.neighbors) == 0 or (len(current.neighbors) == 1 and visited.get(current.neighbors[0].value)):
                possible_paths += 1
    return possible_paths
print(findNumPaths(root, m, vertices))