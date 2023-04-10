s = {'write': 'W', 'read': 'R','execute': 'X'}
dict_prog_list = dict()

for i in range(int(input())):
    prog, *rights = input().split()
    dict_prog_list.setdefault(prog, rights)
for i in range(int(input())):
    request = input().split()

    if s[request[0]] in dict_prog_list[request[1]]:
        print('OK')
    else:
        print("Access denied")