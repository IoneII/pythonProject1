a, b = int(input()), int(input())
list_range = [str(i) for i in range(a, b+1) if '0' not in str(i)]

numbers = filter(lambda x: all([int(x) % int(i) == 0 for i in x]), list_range)
print(*numbers)
