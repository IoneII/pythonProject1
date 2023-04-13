def pretty_print(data, side='-', delimiter='|'):
    count = 0
    for el in data:
        count += 3 + len(str(el))

    print(' ',end='')
    for _ in range(count-1):
        print(side, end='')
    print(' ', end='')
    print()
    print(delimiter, end='')
    for i in data:
       print('', i, delimiter, end='')
    print()
    print(' ', end='')
    for _ in range(count - 1):
        print(side, end='')
    print(' ', end='')
    print()

pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')