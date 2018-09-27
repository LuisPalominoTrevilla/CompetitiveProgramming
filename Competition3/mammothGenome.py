import operator
def decodeGeonma(s, n):
    genomes = {}
    genomes['A'] = 0
    genomes['G'] = 0
    genomes['C'] = 0
    genomes['T'] = 0
    incognitos = 0
    pos_incognitos = []
    for genome in s:
        if genome != '?':
            genomes[genome] +=1
        else:
            incognitos += 1
    MAX = max(genomes.items(), key=operator.itemgetter(1))[0]
    max_value = genomes[MAX] if genomes[MAX] > 0 else 1
    for k in genomes.keys():
        if genomes[k] < max_value:
            while(genomes[k] < max_value):
                incognitos -= 1
                genomes[k]+=1
                pos_incognitos.append(k)
    if incognitos < 0:
        return '==='
    if incognitos > 0 and incognitos%4!=0:
        return '==='
    elif incognitos != 0:
        rest = incognitos//4
        for i in range(rest):
            pos_incognitos.append('A')
            pos_incognitos.append('C')
            pos_incognitos.append('T')
            pos_incognitos.append('G')
    res = ""
    for i in s:
        if i == '?':
            res+=pos_incognitos.pop(0)
        else:
            res += i
    return res
n = int(input())
s = input()
print(decodeGeonma(s, n))