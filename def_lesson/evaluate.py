
from functools import reduce
def evaluate(coefficients, x):
    n = [i for i in range(len(coefficients))[::-1]]
    result = list(map(lambda y, z: y*x**z, coefficients, n))
    return print(reduce(lambda a, b: a+b, result))

evaluate([int(i) for i in input().split()], x=int(input()))

