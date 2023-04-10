


list_num = [int(i) for i in range(int(input()))]
list_del, list_fractions, dict_fractions  = [], [], dict()
for i in range(len(list_num)//2 + 1):
    list_del.append((list_num[i], list_num[-i]))

for i in list_del:
    if i[0] > 0:
        list_fractions.append(Fraction(i[0], i[1]))

max_numerator = max((Fraction(i).numerator) for i in list_fractions) #x - максимальный числитель

for el in list_del:
    dict_fractions[el[0]] = el[1]

print(Fraction(max_numerator, dict_fractions[max_numerator]))

