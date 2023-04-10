with open('goats', 'r') as goats:
    #print(goats.read())
    count = 0
    for i in goats.readlines():
        count += 1
        if 'GOATS' in i:
            num = count -2
            print(num)
    for _ in range(num):
        print(goats.readline())



