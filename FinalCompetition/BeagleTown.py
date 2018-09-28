import math  
def calculateDistance(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist
class Beagle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.possible_fuentes = []
        self.possible_fuentes_hash = {}
    def add_fuente(self, fuente):
        self.possible_fuentes.append(fuente)
        self.possible_fuentes_hash[fuente] = True
class Fuente:
    def __init__(self, x, y, litters):
        self.x = x
        self.y = y
        self.beagles = []
        self.litters = litters
    def remove_litter(self):
        self.litters-=1
        if self.litters == 0:
            for beagle in beagles:
                if beagle.possible_fuentes_hash.get(self):
                    beagle.possible_fuentes.remove(self)
    def add_beagle(self, beagle):
        self.beagles.append(beagle)

n, m, s = [int(x) for x in input().split()]
beagles = []
for i in range(n):
    line = [int(x) for x in input().split()]
    beagle = Beagle(line[0], line[1])
    beagles.append(beagle)
for i in range(m):
    line = [int(x) for x in input().split()]
    fuente = Fuente(line[0], line[1], line[2])
    for j in range(n):
        distance = calculateDistance(beagles[j].x, beagles[j].y, fuente.x, fuente.y)
        if distance + 10 < s:
            beagles[j].add_fuente(fuente)
            fuente.add_beagle(beagles[j])
possible = True
while len(beagles) > 0:
    min_fuentes = beagles[0]
    for i in range(1,len(beagles)):
        if len(beagles[i].possible_fuentes) < len(min_fuentes.possible_fuentes):
            min_fuentes = beagles[i]
    beagles.remove(min_fuentes)
    # Tomar agua
    if len(min_fuentes.possible_fuentes) == 0:
        possible = False
        break
    max_litros = min_fuentes.possible_fuentes[0]
    for j in range(1,len(min_fuentes.possible_fuentes)):
        if min_fuentes.possible_fuentes[j].litters > max_litros.litters:
            max_litros = min_fuentes.possible_fuentes[j]
    max_litros.remove_litter()
print("YES" if possible else "NO")