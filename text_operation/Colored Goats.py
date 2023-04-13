with open('goats.txt', 'r') as goats, open('logfile.txt', 'w') as answer:
    count = 0
    for i in goats.readlines():
        count += 1
        if 'GOATS' in i:
            num = count - 1
    goats.seek(0)
    colors = (goats.readlines()[1:num])
    counts = dict()
    goats.seek(0)
    a = (len(goats.readlines()) - num - 1)
    goats.seek(0)
    for i in goats.readlines()[num+1:]:
        counts[i.strip()] = counts.get(i.strip(), 0) + 1
    print(*sorted([k for k, v in counts.items() if v > a * 0.07]), sep='\n', file=answer)
