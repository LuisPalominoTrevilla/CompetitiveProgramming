class Nodo:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)

n, m = [int(x) for x in input().split()]
vertices = [None] * (n+1)
for i in range(m):
    node1, node2 = [int(x) for x in input().split()]
    if not vertices[node1]:
        vertices[node1] = Nodo(node1)
    if not vertices[node2]:
        vertices[node2] = Nodo(node2)
    vertices[node1].addNeighbor(vertices[node2])
    vertices[node2].addNeighbor(vertices[node1])
def isCthulhu(vertices):
    visited = {}
    work = []
    num_loops = 0
    for vertice in vertices:
        if vertice:
            work.append(vertice)
            break
    while(len(work) > 0):
        current = work.pop()
        visited[current.value] = True
        num_repeated = 0
        for neighbor in current.neighbors:
            if not visited.get(neighbor.value):
                if neighbor not in work:
                    work.insert(0, neighbor)
            else:
                num_repeated +=1
        if num_repeated > 1:
            num_loops +=1
        if num_loops > 1:
            return False
    return num_loops == 1 and len(visited.keys()) == n
if m == 0:
    print("NO")
else:
    print('NO'if not isCthulhu(vertices) else "FHTAGN!")