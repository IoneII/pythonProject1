with open('lines.txt', 'r', encoding='utf-8') as file:
    numbers = []
    for stroka in file:
       for word in stroka.split():
            sum_stroka = (map(lambda x: ' ' if x not in ['1','2','3','4','5','6','7','8','9','0'] else x, word))
            numbers.append((sum(map(int, ''.join(sum_stroka).split()))))
print(sum(numbers))