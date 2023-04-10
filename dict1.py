numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

dict_del = {}
for num in numbers:
    x = []
    for j in range(1, num+1):
        if num % j == 0:
            x.append(j)
            dict_del[num] = x
print(dict_del)

result = {}
result = {num: [j for j in range(1, num + 1) if num %j ==0] for num in numbers}

print(result)