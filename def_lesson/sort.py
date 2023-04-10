from decimal import *
def intrasting_sort(num):
    return sum(Decimal.as_tuple(num)[1]), num

s = input()
s_list = [Decimal(i) for i in s.split()]
print(*sorted(s_list, key=intrasting_sort))

print(intrasting_sort(Decimal(58)))
