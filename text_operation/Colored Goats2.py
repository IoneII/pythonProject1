with open('goats.txt', encoding='utf-8') as file, open('logfile.txt', 'w') as final:
    st = list(map(lambda x: x.strip(), file.readlines()))
    lst = st[1:st.index('GOATS')]
    st = st[st.index('GOATS') + 1:]
    dt = {i: 0 for i in lst}
    for i in st:
        dt[i] += 1
    print(dt)
    res = []
    p = len(st)
    for k, v in dt.items():
        if v > (p * 0.07):
            res.append(k)
    res.sort()

    for i in res:
        print(i, sep='\n', file=final)