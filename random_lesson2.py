import random as r

anagramma = [str(i) for i in input()]
print(*r.sample(anagramma, len(anagramma)), sep='')
r.shuffle(anagramma)
print(*anagramma, sep='')