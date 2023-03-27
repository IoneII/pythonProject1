import random as r
import string
rnd_set = set(r.sample(range(0,76), 25))
A = [[0 for i in range(5)] for j in range(5)]
for i in range(5):
    for j in range(5):
        A[i][j] = (str(rnd_set.pop())).ljust(3)

A[2][2] = ('0').ljust(3)

for i in range(5):
    print(*A[i])
