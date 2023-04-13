list_ip = [input() for i in range(int(input()))]
list_ip = (list(list(int(i) for i in j.split('.'))  for j in list_ip))
for el in sorted(list_ip):
    print(*el, sep='.')
