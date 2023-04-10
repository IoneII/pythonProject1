import random as r

loter = set()
bilet = ''

while len(loter) < 100:
    for i in range(7):
        bilet = bilet + str(r.randint(0, 9))
    loter.add(str(bilet))
    if bilet[0] == '0':
        loter.remove(bilet)
    bilet = ''
print(*loter, sep='\n')