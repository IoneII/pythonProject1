
import math as m
def qrt(num):
    return num**2
def coob(num):
    return num**3
def sqrt_(num):
    return m.sqrt(num)
def abs_(num):
    return abs(num)
def sinus_(num):
    return m.sin(num)

operations = {'квадрат':qrt, 'куб':coob, 'корень':sqrt_, 'модуль':abs_, 'синус':sinus_}
n = int(input())
print((operations[input()](n)))
